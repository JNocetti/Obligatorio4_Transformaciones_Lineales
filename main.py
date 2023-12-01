import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import utils

image = Image.open('images/bully.jpg')

rotatedImage = utils.rotate_image(image, 60)

utils.show_image(rotatedImage)