from PIL import Image

try:
    img = Image.open("Untitled.png").show()
except IOError:
    pass