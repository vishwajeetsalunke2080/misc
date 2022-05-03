from PIL import Image
import requests
import PIL
from io import BytesIO
import io
import os

response = requests.get("https://photos.clarinea.fr/BL_1_fr/none.jpg")
image_bytes = io.BytesIO(response.content)
img = PIL.Image.open(image_bytes)
img.show()