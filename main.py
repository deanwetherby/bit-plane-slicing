import argparse
import logging
import random

import numpy as np
import cv2

logging.basicConfig(level=logging.DEBUG)


def convert_image_to_bit_planes(img, bit_size):
    """
    Convert a color image to separate rgb bit planes

    Parameters:
    img: OpenCV image
    bit_size: 

    Returns
    b_bits: Blue channel bit planes
    g_bits: Green channel bit planes
    r_bits: Red channel bit planes
    
    """

    # split channels in a color (3-channel) image
    b, g, r = cv2.split(img)
    
    # convert image integers to bits assuming 8 bit image for each color channel
    b_bits = np.unpackbits(b).reshape(bit_size)
    g_bits = np.unpackbits(g).reshape(bit_size)
    r_bits = np.unpackbits(r).reshape(bit_size)

    return b_bits, g_bits, r_bits


def convert_bit_planes_to_image(b_bits, g_bits, r_bits, img_size):
    """
    Convert RGB bit planes back into a color image

    Parameters
    b_bits: Blue channel bit planes
    g_bits: Green channel bit planes
    r_bits: Red channel bit planes

    Returns
    img: OpenCV image

    """

    # convert back to 8-bit integer in the original shape
    b_aug = np.packbits(b_bits).reshape(img_size)
    g_aug = np.packbits(g_bits).reshape(img_size)
    r_aug = np.packbits(r_bits).reshape(img_size)

    # combine the channels back into a color image
    return cv2.merge((b_aug, g_aug, r_aug))


def bit_plane_slice(b_bits, g_bits, r_bits, bit_plane_list):
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
            logging.debug('Zeroizing {} bit_plane'.format(int(bit_plane)))
            # zeroize the bit plane in each RGB channel
            b_bits[:,:,int(bit_plane)] = 0
            g_bits[:,:,int(bit_plane)] = 0
            r_bits[:,:,int(bit_plane)] = 0
    

def process_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help="Input image path")
    parser.add_argument('-o', '--output', help="Output image path")
    parser.add_argument('-p', '--plane', nargs='+', help="Space separated list of bit planes to zeroize")
    return parser.parse_args()


def main():

    args = process_arguments()
    logging.debug(args)

    logging.debug("Reading image from {}".format(args.input))
    img = cv2.imread(args.input)

    if img is not None and len(img.shape) == 3 and img.shape[2] == 3:

        height, width, channels = img.shape
        img_size = (height, width)
        bit_size = img_size + (8,)
        logging.debug("Image size: {}".format(img_size + (channels,)))
        logging.debug("Bit size: {}".format(bit_size))

        b_bits, g_bits, r_bits = convert_image_to_bit_planes(img, bit_size)
        bit_plane_slice(b_bits, g_bits, r_bits, args.plane)
        img = convert_bit_planes_to_image(b_bits, g_bits, r_bits, img_size)

        logging.debug("Saving image to {}".format(args.output))
        cv2.imwrite(args.output, img)
    else:
        logging.error("Image was either not read in correctly or is not color.")

if __name__ == '__main__':
    main()


