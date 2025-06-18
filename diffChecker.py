from PIL import Image, ImageChops

img1 = Image.open('First.jpg')
img2 = Image.open('Second.jpg')

difference = ImageChops.difference(img1, img2)
if difference.getbbox():
    difference.show()
    difference.save("difference_output.jpg")
else:
    print("Images are identical.")