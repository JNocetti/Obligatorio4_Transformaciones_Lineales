import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import utils

image = Image.open('images/bully.jpg')

rotatedImage = utils.rotate_image(image, 60)

scaledImage = utils.scaling(image, (10))

shearedImage = utils.shearing(image, (1))


utils.show_image(rotatedImage)
utils.show_image(scaledImage)
utils.show_image(shearedImage)

svdImage = utils.svd(image)

compressImage = utils.compress_image(image, 2)

print(compressImage)

utils.show_image(compressImage)
