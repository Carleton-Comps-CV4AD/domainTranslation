from PIL import Image
try:
    img = Image.open("dataset/75_2.png")
    img.show()
except Exception as e:
    print("Error opening image with Pillow:", e)