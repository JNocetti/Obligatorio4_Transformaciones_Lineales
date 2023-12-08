import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.ndimage import rotate
from PIL import Image
from skimage import io
from skimage import transform as tf
from skimage.color import rgb2gray

def show_image(image, tittle):
    plt.imshow(image,"gray")
    plt.title(tittle)
    plt.show()


def svd(image):
    imageToArray = np.array(image)
    U, S, V = np.linalg.svd(imageToArray, full_matrices=False)
    return U, S, V


def compress_image(image, k):
    image = rgb2gray(image)
    imageToArray = np.array(image)
    U, S, V = np.linalg.svd(imageToArray, full_matrices=False)
    compressed_image = np.dot(U[:, :k], np.dot(np.diag(S[:k]), V[:k, :]))
    return compressed_image


def rotate_image(img, angle):
    img = np.array(img)
    #  convert rotation amount to radian
    rotation_amount_rad = angle * np.pi / 180.0

    #  get dimension info
    height, width, num_channels = img.shape

    #  create output image, for worst case size (45 degree)
    max_len = int(math.sqrt(height*height + width*width))
    rotated_image = np.zeros((max_len, max_len, num_channels))
    #rotated_image = np.zeros((img.shape))

    rotated_height, rotated_width, _ = rotated_image.shape
    mid_row = int( (rotated_height+1)/2 )
    mid_col = int( (rotated_width+1)/2 )

    #  for each pixel in output image, find which pixel
    #it corresponds to in the input image
    for r in range(rotated_height):
        for c in range(rotated_width):
            #  apply rotation matrix, the other way
            y = (r-mid_col)*math.cos(rotation_amount_rad) + (c-mid_row)*math.sin(rotation_amount_rad)
            x = -(r-mid_col)*math.sin(rotation_amount_rad) + (c-mid_row)*math.cos(rotation_amount_rad)

            #  add offset
            y += mid_col
            x += mid_row

            #  get nearest index
            #a better way is linear interpolation
            x = round(x)
            y = round(y)

            #print(r, " ", c, " corresponds to-> " , y, " ", x)

            #  check if x/y corresponds to a valid pixel in input image
            if (x >= 0 and y >= 0 and x < width and y < height):
                rotated_image[r][c][:] = img[y][x][:]


    #  save output image
    output_image = Image.fromarray(rotated_image.astype("uint8"))
    return output_image


def scaling(image, k):
    scaled_image = image.resize(
        (int(image.width * k), int(image.height * k)))
    return scaled_image


def shearing(image, shearInput):
    image = np.array(image)
    afine_tf = tf.AffineTransform(shear=shearInput)
    modified = tf.warp(image, inverse_map=afine_tf)
    return modified



