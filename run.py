import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter

def func():
    image = Image.open("results.png")
    image.filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(image)

print func()

