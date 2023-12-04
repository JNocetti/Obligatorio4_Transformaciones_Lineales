import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import utils

image = Image.open('images/bully.jpg')

rotatedImage = utils.rotate_image(image, 60)

scaledImage = utils.scaling(image, (0.5))

#utils.show_image(rotatedImage)
utils.show_image(scaledImage)