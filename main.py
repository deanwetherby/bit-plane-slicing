import argparse
import logging
import random

from typing import Tuple, List

import numpy as np
import cv2

logging.basicConfig(level=logging.DEBUG)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Input image path")
    parser.add_argument("-o", "--output", help="Output image path")
    parser.add_argument(
        "-p", "--plane", nargs="+", help="Space separated list of bit planes to zeroize"
    )
    return parser.parse_args()


def convert_image_to_bit_planes(
    img: np.ndarray, bit_size: Tuple[int, int, int]
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Convert a color image to separate rgb bit planes

    Parameters:
    img: OpenCV image
    bit_size: image height, width, 8 channels

    Returns
    b_bits: Blue channel bit planes
    g_bits: Green channel bit planes
    r_bits: Red channel bit planes

    """

    # split image into 3 color channels (RGB)
    b, g, r = cv2.split(img)

    # convert 8-bit image integers (0-255) to bits (00000000-11111111)
    # example conversion from integer to bits:
    # >>> np.unpackbits(np.array([2], dtype=np.uint8))
    # array([0, 0, 0, 0, 0, 0, 1, 0], dtype=uint8)
    b_bits = np.unpackbits(b).reshape(bit_size)
    g_bits = np.unpackbits(g).reshape(bit_size)
    r_bits = np.unpackbits(r).reshape(bit_size)

    return b_bits, g_bits, r_bits


def convert_bit_planes_to_image(
    b_bits: np.ndarray,
    g_bits: np.ndarray,
    r_bits: np.ndarray,
    img_size: Tuple[int, int, int],
) -> np.ndarray:
    """
    Convert RGB bit planes back into a color image

    Parameters
    b_bits: Blue channel bit planes
    g_bits: Green channel bit planes
    r_bits: Red channel bit planes
    img_size: Image height, width, 3 color channels

    Returns
    img: OpenCV image
    """

    # convert back to 8-bit integer in the original shape
    # example conversion from bits to integer
    # >>> np.packbits(np.array([0, 0, 0, 0, 0, 0, 1, 0], dtype=np.uint8))
    # array([2], dtype=uint8)
    b_aug = np.packbits(b_bits).reshape(img_size)
    g_aug = np.packbits(g_bits).reshape(img_size)
    r_aug = np.packbits(r_bits).reshape(img_size)

    # combine the color channels back into an image
    return cv2.merge((b_aug, g_aug, r_aug))


def bit_plane_slice(
    b_bits: np.ndarray,
    g_bits: np.ndarray,
    r_bits: np.ndarray,
    bit_plane_list: List[int],
) -> None:
    """
    Zeroize the bit planes in the list for all the rgb bit plane images

    Parameters
    b_bits: Blue channel bit planes
    g_bits: Green channel bit planes
    r_bits: Red channel bit planes
    bit_plane_list: list of channels to zeroize
    """

    if bit_plane_list is not None:
        for bit_plane in bit_plane_list:
            logging.debug(f"Zeroizing {int(bit_plane)} bit_plane")
            # zeroize the bit plane in each RGB channel
            b_bits[:, :, int(bit_plane)] = 0
            g_bits[:, :, int(bit_plane)] = 0
            r_bits[:, :, int(bit_plane)] = 0


def main():
    args = parse_arguments()
    logging.debug(args)

    logging.debug(f"Reading image from {args.input}")
    img = cv2.imread(args.input)

    if img is not None and len(img.shape) == 3 and img.shape[2] == 3:
        height, width, channels = img.shape
        img_size = (height, width)
        bit_size = img_size + (8,)
        logging.debug(f"Image size: {img_size + (channels,)}")
        logging.debug(f"Bit size: {bit_size}")

        b_bits, g_bits, r_bits = convert_image_to_bit_planes(img, bit_size)
        bit_plane_slice(b_bits, g_bits, r_bits, args.plane)
        img = convert_bit_planes_to_image(b_bits, g_bits, r_bits, img_size)

        logging.debug(f"Saving image to {args.output}")
        cv2.imwrite(args.output, img)
    else:
        logging.error("Image was either not read in correctly or is not color.")


if __name__ == "__main__":
    main()
