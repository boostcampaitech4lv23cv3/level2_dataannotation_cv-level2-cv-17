import math
import time
from datetime import timedelta
from pathlib import Path

import torch
import typer
from torch import cuda
from torch.optim import lr_scheduler
from torch.utils.data import DataLoader
from tqdm.rich import tqdm

import wandb
from dataset import SceneTextDataset
from east_dataset import EASTDataset
from logger import get_logger
from model import EAST

# from tqdm import tqdm


DATA_DIR = "/opt/ml/input/data/ICDAR17_Korean/"

logger = get_logger()

wandb.init(project="data-generation", entity="boostcamp-ai-tech-4-cv-17")
# https://wandb.ai/boostcamp-ai-tech-4-cv-17/data-generation
# https://colab.research.google.com/github/wandb/examples/blob/master/colabs/intro/Intro_to_Weights_%26_Biases.ipynb#scrollTo=q4HuW-12PkE5


def input_size_callback(input_size: int):
    if input_size % 32 != 0:
        raise typer.BadParameter("`input_size` must be a multiple of 32")

    return input_size


def main(
    data_dir: str = DATA_DIR,
    model_dir: str = "trained_models",
    device: str = "cuda" if cuda.is_available() else "cpu",
    image_size: int = 1024,
    input_size: int = typer.Option(512, callback=input_size_callback),
    num_workers: int = 4,
    batch_size: int = 12,
    learning_rate: float = 1e-3,
    max_epoch: int = 200,
    save_interval: int = 5,
):
    logger.info(
        f"train.py --data-dir '{data_dir}' --model-dir '{model_dir}' --device '{device}' --image-size {image_size} --input-size {input_size} --num-workers {num_workers} --batch-size {batch_size} --learning-rate {learning_rate} --max-epoch {max_epoch} --save-interval {save_interval}"
    )

    wandb.config.update(
        {
            "data_dir": data_dir,
            "model_dir": model_dir,
            "device": device,
            "image_size": image_size,
            "input_size": input_size,
            "num_workers": num_workers,
            "batch_size": batch_size,
            "learning_rate": learning_rate,
            "max_epoch": max_epoch,
            "save_interval": save_interval,
        }
    )

    dataset = SceneTextDataset(
        data_dir, split="train", image_size=image_size, crop_size=input_size
    )
    dataset = EASTDataset(dataset)
    num_batches = math.ceil(len(dataset) / batch_size)
    train_loader = DataLoader(
        dataset, batch_size=batch_size, shuffle=True, num_workers=num_workers
    )

    model = EAST()
    model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    scheduler = lr_scheduler.MultiStepLR(
        optimizer, milestones=[max_epoch // 2], gamma=0.1
    )

    model.train()
    for epoch in range(max_epoch):
        epoch_loss, epoch_start = 0, time.perf_counter()
        progress = f"[Epoch {epoch + 1}/{max_epoch}]"

        with tqdm(total=num_batches) as pbar:
            for img, gt_score_map, gt_geo_map, roi_mask in train_loader:
                pbar.set_description(progress)

                loss, extra_info = model.train_step(
                    img, gt_score_map, gt_geo_map, roi_mask
                )
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                loss_val = loss.item()
                epoch_loss += loss_val

                pbar.update(1)
                pbar.set_postfix(
                    {
                        "Cls loss": extra_info["cls_loss"],
                        "Angle loss": extra_info["angle_loss"],
                        "IoU loss": extra_info["iou_loss"],
                    }
                )

        scheduler.step()

        mean_loss = epoch_loss / num_batches
        elapsed_time = timedelta(seconds=time.perf_counter() - epoch_start)
        logger.info(
            f"{progress} Mean loss: {mean_loss:.4f} | Elapsed time: {elapsed_time}"
        )
        wandb.log(
            {
                "Mean loss": mean_loss,
                "Elapsed time": elapsed_time,
            }
        )

        if (epoch + 1) % save_interval == 0:
            model_dir_path = Path(model_dir)
            model_dir_path.mkdir(parents=True, exist_ok=True)

            torch.save(model.state_dict(), model_dir_path / "latest.pth")


if __name__ == "__main__":
    typer.run(main)
