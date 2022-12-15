import json
import math
import os.path as osp
from argparse import ArgumentParser

import numpy as np
from tqdm import tqdm


def parse_args():
    parser = ArgumentParser(
        description="Add error(=shake) to the bounding box points by the given ratio."
    )

    parser.add_argument(
        "--anno_path", type=str, help="path of the annotation file in UFO format"
    )
    parser.add_argument(
        "--ratio",
        type=float,
        default=0.125,
        help="ratio of the distance of point moved to the square root of the bounding box area",
    )
    parser.add_argument(
        "--suffix",
        type=str,
        default="_shaked",
        help="suffix for the new json file name",
    )

    args = parser.parse_args()

    return args


def generate_new_file_name(current_path, suffix):
    current_name = osp.split(current_path)[1].split(".")[0]
    new_name = current_name + suffix
    new_path = osp.join(osp.split(current_path)[0], new_name + ".json")
    return new_path


def get_polygon_area(points):
    n_points = len(points)
    area = 0
    for i in range(n_points):
        # current, next x and y
        cx = points[i][0]
        cy = points[i][1]
        nx = points[(i + 1) % n_points][0]
        ny = points[(i + 1) % n_points][1]
        area += cx * ny - cy * nx

    return int(abs(area / 2.0))


def shift_point(point, width, height, sigma):
    clip = lambda x, max: 0 if x < 0 else max if x > max else x
    dist = np.random.normal(0, sigma)
    theta = np.random.uniform(0, 2 * math.pi)

    x = point[0] + dist * math.cos(theta)
    y = point[1] + dist * math.sin(theta)

    x = clip(x, width)
    y = clip(y, height)

    return [x, y]


def shake_bbox(points, width, height, ratio=0.125):
    sigma = math.sqrt(get_polygon_area(points)) * ratio

    new_points = []
    for point in points:
        new_point = shift_point(point, width, height, sigma)
        new_points.append(new_point)

    return new_points


def do_shaking(anno_path, ratio, suffix):
    ufo = json.load(open(anno_path, "r"))

    for image_name in tqdm(ufo["images"]):
        image = ufo["images"][image_name]
        width = image["img_w"]
        height = image["img_h"]
        for word_tag in image["words"]:
            points = image["words"][word_tag]["points"]
            epoints = shake_bbox(points, width, height, ratio)
            ufo["images"][image_name]["words"][word_tag]["points"] = epoints

    new_path = generate_new_file_name(anno_path, suffix)
    json.dump(ufo, open(new_path, "w"), indent=4)


def main(args):
    do_shaking(**args.__dict__)


if __name__ == "__main__":
    args = parse_args()
    main(args)
