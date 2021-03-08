from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from PIL import Image
import sys

class Conversor:

    def convertirA(self, rutaOrigen,rutaSinExtension,extension):
        if extension == "jpg":
            imagenIn = Image.open(rutaOrigen)
            rgb_im = imagenIn.convert('RGB')
            rutaDestino = asksaveasfilename(initialfile="nombreArchivo.png",defaultextension=".png",filetypes = (("png files","*.png"),("gif files","*.gif"),("bmp files","*.bmp"),("all files","*.*")))
            #  rutaDestino=rutaSinExtension+'.png'
            rgb_im.save(rutaDestino, quality=95)
            image1 = Image.open(rutaDestino)
            image1.show()


        elif extension == "png":
            imagenIn = Image.open(rutaOrigen)
            rgb_im = imagenIn.convert('RGB')
            rutaDestino = asksaveasfilename(initialfile="nombreArchivo.png",defaultextension=".png",filetypes = (("jpeg files","*.jpg"),("gif files","*.gif"),("bmp files","*.bmp"),("all files","*.*")))
            #  rutaDestino=rutaSinExtension+'.png'
            rgb_im.save(rutaDestino, quality=95)
            image1 = Image.open(rutaDestino)
            image1.show()
       
            
        elif extension == "gif":
            imagenIn = Image.open(rutaOrigen)
            rgb_im = imagenIn.convert('RGB')
            rutaDestino = asksaveasfilename(initialfile="nombreArchivo.png",defaultextension=".png",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("bmp files","*.bmp"),("all files","*.*")))
            #  rutaDestino=rutaSinExtension+'.png'
            rgb_im.save(rutaDestino, quality=95)
            image1 = Image.open(rutaDestino)
            image1.show()
       
        elif extension == "bmp":
            imagenIn = Image.open(rutaOrigen)
            rgb_im = imagenIn.convert('RGB')
            rutaDestino = asksaveasfilename(initialfile="nombreArchivo.png",defaultextension=".png",filetypes = (("jpeg files","*.jpg"),("gif files","*.gif"),("png files","*.png"),("all files","*.*")))
            #  rutaDestino=rutaSinExtension+'.png'
            rgb_im.save(rutaDestino, quality=95)
            image1 = Image.open(rutaDestino)
            image1.show()
       

    
   
    
print("Desea convertir alguna imagen ?")
print("presione s para si")
print("presione n para no")

respuesta=input("Escribe tu respuesta ")
hola=Tk()
if respuesta == "s":
    # we don't want a full GUI, so keep the root window from appearing
    rutaOrigen = askopenfilename(filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("gif files","*.gif"),("bmp files","*.bmp"),("all files","*.*"))) # show an "Open" dialog box and return the path to the selected file
    hola.withdraw()
    print("Ruta de origen: "+rutaOrigen+"\n")


    rutaOrigenDividida=rutaOrigen.split(".")
    rutaSinExtension=rutaOrigenDividida[0]#ruta sin extension de archivo seleccionado
    extension=rutaOrigenDividida[-1]#extension de archivo seleccionado
    print(rutaSinExtension)

    print("La extension de la imagen seleccionada es  ."+extension+"\n")

    

    convertir = Conversor()

    convertir.convertirA(rutaOrigen,rutaSinExtension,extension)

   
    
       

            
    #imagenIn = Image.open(filename)
    #rgb_im = imagenIn.convert('RGB')
    #rgb_im.save(rse+'.bmp', quality=95)
    #imagenOut=rse+'.bmp'
    #imagenOut.show()

else:
   sys.exit()
