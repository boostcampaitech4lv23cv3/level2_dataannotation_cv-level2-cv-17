import json
import math
import os.path as osp
from argparse import ArgumentParser

import numpy as np
from tqdm import tqdm


def parse_args():
    parser = ArgumentParser(
        description="Loose or shrink bounding box by the given ratio."
    )

    parser.add_argument(
        "--anno_path", type=str, help="path of the annotation file in UFO format."
    )
    parser.add_argument(
        "--ratio",
        type=float,
        default=1.0,
        help="ratio of the area of resuling bounding box to that of the original one.",
    )
    parser.add_argument(
        "--suffix",
        type=str,
        default="_expanded",
        help="suffix for the new json file name",
    )

    args = parser.parse_args()

    return args


def generate_new_file_name(current_path, suffix):
    current_name = osp.split(current_path)[1].split(".")[0]
    new_name = current_name + suffix
    new_path = osp.join(osp.split(current_path)[0], new_name + ".json")
    return new_path


def get_polygon_centroid(points):
    return np.mean(points, axis=0)


def expand_bbox(points, ratio, width, height):
    def clip(x, max):
        if x < 0:
            return 0
        else:
            return max if x > max else x

    center = get_polygon_centroid(points)

    new_points = []
    for point in points:
        vector = point - center
        new_point = center + vector * math.sqrt(ratio)
        new_point[0] = clip(new_point[0], width)
        new_point[1] = clip(new_point[1], height)
        new_points.append(new_point.tolist())

    return new_points


def do_expansion(anno_path, ratio, suffix):
    ufo = json.load(open(anno_path))

    for image_name in tqdm(ufo["images"]):
        image = ufo["images"][image_name]
        width = image["img_w"]
        height = image["img_h"]
        for word_tag in image["words"]:
            points = image["words"][word_tag]["points"]
            epoints = expand_bbox(points, ratio, width, height)
            ufo["images"][image_name]["words"][word_tag]["points"] = epoints

    new_path = generate_new_file_name(anno_path, suffix)
    json.dump(ufo, open(new_path, "w"), indent=4)


def main(args):
    do_expansion(**args.__dict__)


if __name__ == "__main__":
    args = parse_args()
    main(args)
