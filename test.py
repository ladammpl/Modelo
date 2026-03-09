import qrcode

text = input("ingresa texto:  ")
nombre_img = input("ingresa el nombre de la imagen  ")

img = qrcode.make(text)
img.save(nombre_img + ".png")
