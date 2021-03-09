# PYTHON CONVERSOR_SHELL 

* **Librerias Importadas**

***Pillow, la biblioteca Python para tratamiento de imágenes***

Pillow es una biblioteca para el tratamiento y edición de imágenes que hereda de PIL. Pillow soporta gran cantidad de formatos de imagen, entre ellos, los más comunes: JPG, PNG y GIF.

$> pip install pillow

Se ejecuta este comando en Python para importar la libreria de Pillow, antes de ejecutar la aplicación.


* **Comentarios Código Aplicación Shell Lenguaje Python**

    **from PIL import Image** Se está importando la libreria. El módulo (Image) proporciona una clase con el mismo nombre que se utiliza para representar una imagen PIL. El módulo también proporciona una serie de funciones de fábrica, incluidas funciones para cargar imágenes desde archivos y crear nuevas imágenes.
                      
    **import os** El módulo nos permite acceder a funcionalidades dependientes del Sistema Operativo, sobre todo, aquellas que nos refieren información sobre el entorno del mismo y nos permiten manipular la estructura de directorios (para leer y escribir archivos).
          
    **import sys** Este módulo provee acceso a algunas variables usadas o mantenidas por el intérprete y a funciones que interactúan fuertemente con el intérprete.


***Clase donde están las funciones correspondientes para realizar la conversion para el tipo de imagen PNG, JPG, GIF y BMP.***
     
     class Conversor:


**Metodo para convertir a .png**

    def convertirApng(self, rutaOrigen,rutaSinExtension):
    
        imagenIn = Image.open(rutaOrigen)                            Abre he identifica el archivo de imagen dado. 
        rgb_im = imagenIn.convert('RGB')                             El modo de la imagen se convierte a RGB (Píxeles de 3x8 bits, color verdadero). 
        rutaDestino=rutaSinExtension+'.png'                          La ruta sin extension es concatenada a el formato de imagen a convertir.
        rgb_im.save(rutaDestino, quality=95)                         La imagen se guarda con el nombre de archivo indicado y quality establece la calidad de la imagen.
        print("El archivo se guardo de forma exitosa en la siguiente ruta "+rutaDestino)                 Imprime la ruta donde quedo la imagen.
        os.startfile(rutaDestino)                                    Abre el archivo con su programa asociado.
        
        

Los siguientes metodos convertidores no se les hace comentarios ya que comparten las mismas lineas de código con el metodo .png anteriormente explicado, con la diferencia que cada metodo se modifica a la extencion especifica diferente. 

**Metodo para convertir a .jpg**

    def convertirAjpg(self, rutaOrigen,rutaSinExtension):
        imagenIn = Image.open(rutaOrigen)
        rgb_im = imagenIn.convert('RGB')
        rutaDestino=rutaSinExtension+'.jpg'
        rgb_im.save(rutaDestino, quality=95)
        print("El archivo se guardo de forma exitosa en la siguiente ruta "+rutaDestino)        
        os.startfile(rutaDestino)
        
**Metodo para convertir a .gif**

    def convertirAgif(self, rutaOrigen,rutaSinExtension):
        imagenIn = Image.open(rutaOrigen)
        rgb_im = imagenIn.convert('RGB')
        rutaDestino=rutaSinExtension+'.gif'
        rgb_im.save(rutaDestino, quality=95)
        print("El archivo se guardo de forma exitosa en la siguiente ruta "+rutaDestino)      
        os.startfile(rutaDestino)

**Metodo para convertir a .bmp**

    def convertirAbmp(self, rutaOrigen,rutaSinExtension):
        imagenIn = Image.open(rutaOrigen)
        rgb_im = imagenIn.convert('RGB')
        rutaDestino=rutaSinExtension+'.bmp'
        rgb_im.save(rutaDestino, quality=95)
        print("El archivo se guardo de forma exitosa en la siguiente ruta "+rutaDestino)
        os.startfile(rutaDestino)
        
        
**Metodo para convertir Imagen**        

    def convertirImagen(self):    
        c=Conversor()                                                                     Instancia de la clase
        print("\n¿Desea convertir alguna imagen ?")                                       Se imprime pregunta
        print("Presione s para si")                                                       Se imprimen opciones
        print("Presione n para no\n")

        respuesta=input("Escribe tu respuesta: ")                                         Se toma la respuesta

        if respuesta == "s":                                                              Si la respuesta es afirmativa toma este camino
            
            rutaOrigen=input("\nIngrese la ruta de la imagen que desea convertir: ")      Se captura la ruta de la imagen a convertir
            


            rutaOrigenDividida=rutaOrigen.split(".")#La ruta se divide a partir del "."
            rutaSinExtension=rutaOrigenDividida[0]#ruta sin extension de archivo seleccionado
            ext=rutaOrigenDividida[-1]#extension de archivo seleccionado
    
            print("La extension de la imagen seleccionada es  ."+ext+"\n")#Imprime la extension del archivo        
            
                     



        
        
