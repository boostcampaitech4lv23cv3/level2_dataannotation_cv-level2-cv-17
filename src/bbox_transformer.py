import json
import math
import os
import os.path as osp
from argparse import ArgumentParser

import cv2
import numpy as np
from tqdm import tqdm


def parse_args():
    parser = ArgumentParser(
        description="Apply projective transformation to all legible bounding boxes."
    )

    parser.add_argument(
        "--anno_path", type=str, help="path of the annotation file in UFO format."
    )
    parser.add_argument("--data_dir", type=str, help="parent directory of the images")
    parser.add_argument(
        "--suffix", type=str, default="_warped", help="suffix for the new file name"
    )

    args = parser.parse_args()

    return args


def get_rotate_mat(theta):
    return np.array(
        [[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]]
    )


def rotate_bbox(bbox, theta, anchor=None):
    points = bbox.T
    if anchor is None:
        anchor = points[:, :1]
    rotated_points = np.dot(get_rotate_mat(theta), points - anchor) + anchor
    return rotated_points.T


def calc_error_from_rect(bbox):
    """Calculate the difference between the vertices orientation and default orientation

    Default orientation is
        x1y1 : left-top,
        x2y2 : right-top,
        x3y3 : right-bot,
        x4y4 : left-bot.
    """
    x_min, y_min = np.min(bbox, axis=0)
    x_max, y_max = np.max(bbox, axis=0)
    rect = np.array(
        [[x_min, y_min], [x_max, y_min], [x_max, y_max], [x_min, y_max]],
        dtype=np.float32,
    )
    return np.linalg.norm(bbox - rect, axis=0).sum()


def find_min_rect_angle(bbox, rank_num=10):
    """
    Find the best angle to rotate poly and obtain min rectangle.
    """
    areas = []
    angles = np.arange(-90, 91) / 180 * math.pi
    for theta in angles:
        rotated_bbox = rotate_bbox(bbox, theta)
        x_min, y_min = np.min(rotated_bbox, axis=0)
        x_max, y_max = np.max(rotated_bbox, axis=0)
        areas.append((x_max - x_min) * (y_max - y_min))

    best_angle, min_error = -1, float("inf")
    for idx in np.argsort(areas)[:rank_num]:
        rotated_bbox = rotate_bbox(bbox, angles[idx])
        error = calc_error_from_rect(rotated_bbox)
        if error < min_error:
            best_angle, min_error = angles[idx], error

    return best_angle


def get_rbox(bbox):
    bbox_points = np.array(bbox, np.int32)
    anchor = bbox_points.T[:, :1]

    # Get the optimal angle
    theta = find_min_rect_angle(bbox_points)

    # Rotate bbox
    rotated_bbox_points = rotate_bbox(bbox_points, theta)

    # Get the circumscribing rectangle
    x_min, y_min = np.min(rotated_bbox_points, axis=0)
    x_max, y_max = np.max(rotated_bbox_points, axis=0)
    circumscribing_rect_points = np.array(
        [[x_min, y_min], [x_max, y_min], [x_max, y_max], [x_min, y_max]]
    )

    # Get the RBOX
    rbox_points = rotate_bbox(circumscribing_rect_points, -theta, anchor=anchor)

    return rbox_points


def warp_bbox_into_rbox(image, bbox, rbox):
    original_size = [pix for pix in image.shape[:2]]

    bbox_points = np.array(bbox, np.float32)
    rbox_points = np.array(rbox, np.float32)

    # Warp perspective
    mtrx_persp = cv2.getPerspectiveTransform(bbox_points, rbox_points)
    roi = cv2.warpPerspective(image, mtrx_persp, original_size[::-1])

    # ROI image
    mask = cv2.fillPoly(
        np.zeros(original_size), [rbox_points.astype(np.int32).reshape((-1, 1, 2))], 1
    )
    roi = cv2.bitwise_and(
        roi.astype(np.uint8), roi.astype(np.uint8), mask=mask.astype(np.uint8)
    )

    # Cut off original bbox
    inverted_mask = cv2.fillPoly(
        np.ones(original_size), [rbox_points.astype(np.int32).reshape((-1, 1, 2))], 0
    )
    image = cv2.bitwise_and(
        image.astype(np.uint8),
        image.astype(np.uint8),
        mask=inverted_mask.astype(np.uint8),
    )

    # Desired output
    image = cv2.bitwise_or(image.astype(np.uint8), roi.astype(np.uint8))

    return image


def warp_dataset(in_anno_path, in_data_dir, suffix):
    # Load annotation file and generate new annotation data
    anno_dir = osp.split(in_anno_path)[0]
    out_anno_name = osp.split(in_anno_path)[1].split(".")[0] + suffix + ".json"
    out_anno_path = osp.join(anno_dir, out_anno_name)
    in_anno = json.load(open(in_anno_path))
    out_anno = {"images": dict()}

    # List image names
    image_names = [name for name in in_anno["images"]]

    # Make directory to save new images
    if in_data_dir.endswith("/"):
        in_data_dir = in_data_dir[:-1]
    parent_data_dir = osp.split(in_data_dir)[0]
    out_folder_name = osp.split(in_data_dir)[1] + suffix
    out_data_dir = osp.join(parent_data_dir, out_folder_name)
    if not osp.exists(out_data_dir):
        os.mkdir(out_data_dir)

    # Transform images and save the result
    for in_image_name in tqdm(image_names):
        # Generate input and output image paths
        name = osp.split(in_image_name)[1]
        in_image_path = osp.join(in_data_dir, name)
        out_image_name = osp.join(out_folder_name, name)
        out_image_path = osp.join(out_data_dir, name)

        # Read image
        image = cv2.imread(in_image_path)
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Apply projective transformation
        words = in_anno["images"][in_image_name]["words"]
        for word in words:
            if words[word]["illegibility"]:
                continue

            # Apply projectivate transformation to the image
            bbox = words[word]["points"]
            rbox = get_rbox(bbox)
            image = warp_bbox_into_rbox(image, bbox, rbox)

            # Revise annotation file
            words[word]["points"] = rbox.tolist()

        out_anno["images"][out_image_name] = in_anno["images"][in_image_name]

        if not cv2.imwrite(out_image_path, image):
            raise Exception(f"Failed to write image '{out_image_path}'.")

    json.dump(out_anno, open(out_anno_path, "w"), indent=4)


def main(args):
    assert args.anno_path is not None and args.data_dir is not None
    anno_path = args.anno_path
    data_dir = args.data_dir
    suffix = args.suffix
    warp_dataset(anno_path, data_dir, suffix)


if __name__ == "__main__":
    args = parse_args()
    main(args)
