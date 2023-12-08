import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import utils

image = Image.open('images/bully.jpg')

rotatedImage = utils.rotate_image(image, 60)
rotatedImage2 = utils.rotate_image(image, 90)


scaledImage = utils.scaling(image, (10))
scaledImage2 = utils.scaling(image, (20))


shearedImage = utils.shearing(image, (1))
shearedImage2 = utils.shearing(image, (100))



utils.show_image(rotatedImage,"Imagen rotada 60 grados")
utils.show_image(rotatedImage2,"Imagen rotada 90 grados")

utils.show_image(scaledImage,"Imagen escalada con k = 10")
utils.show_image(scaledImage2,"Imagen escalada con k = 20")

utils.show_image(shearedImage, "Imagen con shearing 1")
utils.show_image(shearedImage2, "Imagen con shearing 100")


svdImage = utils.svd(image)


compressImage = utils.compress_image(image, 200)
utils.show_image(compressImage, "Imagen comprimida con k = 200")
compressImage = utils.compress_image(image, 20)
utils.show_image(compressImage, "Imagen comprimida con k = 20")
compressImage = utils.compress_image(image, 2)
utils.show_image(compressImage, "Imagen comprimida con k = 2")
compressImage = utils.compress_image(image, 1)
utils.show_image(compressImage, "Imagen comprimida con k = 1")