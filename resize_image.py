from PIL import Image

im = Image.open("./cloud_shape.png")

width, height = im.size
print(width, height)

# left, upper combo gives the upper left corner coordinates
# right, lower combo gives the lower right corner coordinates
def crop_image(im: Image, left, upper, right, lower):
    im2 = im.crop((left, upper, right, lower))
    im2.show()
    return im2

def resize_image(im:Image, width, height):
    im1 = im.resize((width, height))
    im1.show()
    return im1

def save_image(im:Image, filename):
    im.save(filename)

cropped = crop_image(im, 210, 210, 420, 420)
resized = resize_image(im, width//2, height//2)

save_image(cropped, "cropped.png")
save_image(resized, "resized.png")