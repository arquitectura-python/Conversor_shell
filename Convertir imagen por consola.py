from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from PIL import Image
import sys

class Conversor:

    def convertirApng(self, rutaOrigen,rutaSinExtension):
        imagenIn = Image.open(rutaOrigen)
        rgb_im = imagenIn.convert('RGB')
        rutaDestino = asksaveasfilename(initialfile="nombreArchivo.png",defaultextension=".png",filetypes = (("png files","*.png"),("all files","*.*")))
        #  rutaDestino=rutaSinExtension+'.png'
        rgb_im.save(rutaDestino, quality=95)
        image1 = Image.open(rutaDestino)
        image1.show()

    def convertirAjpg(self, rutaOrigen,rutaSinExtension):
        imagenIn = Image.open(rutaOrigen)
        rgb_im = imagenIn.convert('RGB')
        rutaDestino = asksaveasfilename(initialfile="nombreArchivo.jpg",defaultextension=".jpg",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        # rutaDestino=rutaSinExtension+'.jpg'
        rgb_im.save(rutaDestino, quality=95)
        image1 = Image.open(rutaDestino)
        image1.show()
        
    def convertirAgif(self, rutaOrigen,rutaSinExtension):
        imagenIn = Image.open(rutaOrigen)
        rgb_im = imagenIn.convert('RGB')
        rutaDestino = asksaveasfilename(initialfile="nombreArchivo.gif",defaultextension=".gif",filetypes = (("gif files","*.gif"),("all files","*.*")))
        #rutaDestino=rutaSinExtension+'.gif'
        rgb_im.save(rutaDestino, quality=95)
        image1 = Image.open(rutaDestino)
        image1.show()
        
    def convertirAbmp(self, rutaOrigen,rutaSinExtension):
        imagenIn = Image.open(rutaOrigen)
        rgb_im = imagenIn.convert('RGB')
        rutaDestino = asksaveasfilename(initialfile="nombreArchivo.bmp",defaultextension=".bmp",filetypes = (("bmp files","*.bmp"),("all files","*.*")))
        #rutaDestino=rutaSinExtension+'.bmp'
        rgb_im.save(rutaDestino, quality=95)
        image1 = Image.open(rutaDestino)
        image1.show()
   
    
print("Desea convertir alguna imagen ?")
print("presione s para si")
print("presione n para no")

respuesta=input("Escribe tu respuesta ")

if respuesta == "s":
    Tk() # we don't want a full GUI, so keep the root window from appearing
    rutaOrigen = askopenfilename(filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("gif files","*.gif"),("bmp files","*.bmp"),("all files","*.*"))) # show an "Open" dialog box and return the path to the selected file
    print(rutaOrigen)


    rutaOrigenDividida=rutaOrigen.split(".")
    rutaSinExtension=rutaOrigenDividida[0]#ruta sin extension de archivo seleccionado
    ext=rutaOrigenDividida[1]#extension de archivo seleccionado
    print(rutaSinExtension)

    print("La extension de la imagen seleccionada es  ."+ext)
    
    

    convertir = Conversor()

    

   
    if ext == "jpg":
        print("Puede seleccionar la siguientes opciones a convertir \n 1.png \n 2.gif \n 3.bmp")
        numero=int(input("ingrese el numero "))
        if numero == 1:
            convertir.convertirApng(rutaOrigen,rutaSinExtension)
            
        elif numero == 2:
            convertir.convertirAgif(rutaOrigen,rutaSinExtension)
            
        else:
            convertir.convertirAbmp(rutaOrigen,rutaSinExtension)         



    elif ext == "png":
        print("Puede seleccionar la siguientes opciones a convertir \n 1.jpg \n 2.gif \n 3.bmp")
        numero=int(input("ingrese el numero "))
        if numero == 1:
            convertir.convertirAjpg(rutaOrigen,rutaSinExtension)
            
        elif numero == 2:
            convertir.convertirAgif(rutaOrigen,rutaSinExtension)
            
        else:
            convertir.convertirAbmp(rutaOrigen,rutaSinExtension)

            
            
    elif ext == "gif":
        print("Puede seleccionar la siguientes opciones a convertir \n 1.jpg \n 2.png \n 3.bmp")
        numero=int(input("ingrese el numero "))
        if numero == 1:
            convertir.convertirAjpg(rutaOrigen,rutaSinExtension)
            
        elif numero == 2:
            convertir.convertirApng(rutaOrigen,rutaSinExtension)
            
        else:
            convertir.convertirAbmp(rutaOrigen,rutaSinExtension)

            
    elif ext == "bmp":
        print("Puede seleccionar la siguientes opciones a convertir \n 1.jpg \n 2.png \n 3.gif")
        numero=int(input("ingrese el numero "))
        if numero == 1:
            convertir.convertirAjpg(rutaOrigen,rutaSinExtension)
            
        elif numero == 2:
            convertir.convertirApng(rutaOrigen,rutaSinExtension)
            
        else:
            convertir.convertirAgif(rutaOrigen,rutaSinExtension)

            
    #imagenIn = Image.open(filename)
    #rgb_im = imagenIn.convert('RGB')
    #rgb_im.save(rse+'.bmp', quality=95)
    #imagenOut=rse+'.bmp'
    #imagenOut.show()

else:
   sys.exit()
