# image Module
# pillow is to work with image in python
# like we can :
# open image,save image,resize image,rotate image,crop image,format image
# image info.,filter apply
# pillow is third party module
from PIL import Image
#img=Image.open("temple.jpg")

from PIL import Image

#img = Image.open(r"C:\Users\ARYAN-VERMA\OneDrive\Desktop\temple.jpg")
#img.show()
img=Image.open("download (1).jpg")           #it will open image if image is in folder then give image name ("image_name.jpg") otherwise photo path is given (r"")
#img.show()         #it shows the image given
print(img)      #it will give image format,image color=(RGB),size = a X b ,and its location in memory

# image information
print(img.size)
print(img.format)
print(img.mode)

# image resize
img = img.resize((500,500))   #it resize the height and width of image
img.show()  #show image after resize

#rotate
img=img.rotate(90)  #it rotates the image to a specific angle
img.show()

#image flip
# img=img.transpose(Image.FLIP_LEFT_RIGHT)        #flip image from left to right
img=img.transpose(Image.FLIP_TOP_BOTTOM)
img.show()


img.save("Kedarnath.jpg")         #ye current working directory mein save kardega modified image ko

img.show()


'''
| Topic                | Functions/Methods                    |
| -------------------- | ------------------------------------ |
| 📂 Open/Save         | `Image.open()`, `save()`             |
| 👀 Display           | `show()`                             |
| ℹ️ Information       | `size`, `format`, `mode`             |
| 📏 Resize            | `resize()`, `thumbnail()`            |
| 🔄 Rotate            | `rotate()`                           |
| 🪞 Flip              | `transpose()`                        |
| ✂️ Crop              | `crop()`                             |
| 🎨 Color             | `convert()`                          |
| 🖼️ New Image         | `Image.new()`                        |
| 🔲 Pixel work        | `getpixel()`, `putpixel()`           |
| 🌓 Effects/Filters   | `ImageFilter`                        |
| 🔧 Image operations  | `ImageOps`                           |
| 🔀 Merge images      | `Image.blend()`, `Image.composite()` |
| 📐 Transform         | `transform()`                        |
| 📄 Format conversion | JPG ↔ PNG ↔ WEBP etc.                |
'''