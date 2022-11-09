from PIL import Image
from numpy import asarray

from cnn.layers import Conv2D

image_path = "data/Porsche_072.jpg"

image = Image.open(image_path)
# image = image.resize((125,125))
# image_array = asarray(image)

image.show()