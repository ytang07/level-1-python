from PIL import Image

im = Image.open("./cloud_shape.png")

width, height = im.size
print(width, height)

im2 = im.crop((210, 210, 420, 420))
im2.show()

im1 = im.resize((width//2, height//2))
im1.show()
