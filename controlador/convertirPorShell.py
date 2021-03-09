from PIL import Image #El Image módulo proporciona una clase con el mismo nombre que se utiliza para representar una imagen PIL.
                      #El módulo también proporciona una serie de funciones de fábrica,
                      #incluidas funciones para cargar imágenes desde archivos y crear nuevas imágenes.
import os #El módulo os nos permite acceder a funcionalidades dependientes del Sistema Operativo. Sobre todo,
          #aquellas que nos refieren información sobre el entorno del mismo y nos permiten manipular la estructura de directorios (para leer y escribir archivos).
import sys#Este módulo provee acceso a algunas variables usadas o mantenidas por el intérprete y a funciones que interactúan fuertemente con el intérprete.

#Clase donde estaran las funciones correspondientes la conversion del tipo de imagen. 
class Conversor:

        #Convertir a png
    def convertirApng(self, rutaOrigen,rutaSinExtension):
        imagenIn = Image.open(rutaOrigen)# Abre e identifica el archivo de imagen dado. 
        rgb_im = imagenIn.convert('RGB')# El modo de la imagen se convierte a RGB (Píxeles de 3x8 bits, color verdadero)    
        rutaDestino=rutaSinExtension+'.png'#La ruta sin extension es concatenada a el formato de imagen a convertir.
        rgb_im.save(rutaDestino, quality=95)#La imagen se guarda con el nombre de archivo indicado y quality establece la calidad de la imagen.
                                            #Usar el factor de calidad en 95 debería ser suficiente para preservar la calidad de la imagen.
        print("El archivo se guardo de forma exitosa en la siguiente ruta "+rutaDestino)#imprime la ruta donde quedo la imagen.
        os.startfile(rutaDestino)# Abre el archivo con su programa asociado

        #Convertir a jpg
    def convertirAjpg(self, rutaOrigen,rutaSinExtension):
        imagenIn = Image.open(rutaOrigen)
        rgb_im = imagenIn.convert('RGB')
        rutaDestino=rutaSinExtension+'.jpg'
        rgb_im.save(rutaDestino, quality=95)
        print("El archivo se guardo de forma exitosa en la siguiente ruta "+rutaDestino)        
        os.startfile(rutaDestino)
        
        #Convertir a gif
    def convertirAgif(self, rutaOrigen,rutaSinExtension):
        imagenIn = Image.open(rutaOrigen)
        rgb_im = imagenIn.convert('RGB')
        rutaDestino=rutaSinExtension+'.gif'
        rgb_im.save(rutaDestino, quality=95)
        print("El archivo se guardo de forma exitosa en la siguiente ruta "+rutaDestino)      
        os.startfile(rutaDestino)

        #Convertir a bmp
    def convertirAbmp(self, rutaOrigen,rutaSinExtension):
        imagenIn = Image.open(rutaOrigen)
        rgb_im = imagenIn.convert('RGB')
        rutaDestino=rutaSinExtension+'.bmp'
        rgb_im.save(rutaDestino, quality=95)
        print("El archivo se guardo de forma exitosa en la siguiente ruta "+rutaDestino)
        os.startfile(rutaDestino)

    def convertirImagen(self):
        c=Conversor()#Instancia de clase
        print("\n¿Desea convertir alguna imagen ?")#Se imprime pregunta
        print("Presione s para si")                #Se imprimen opciones
        print("Presione n para no\n")

        respuesta=input("Escribe tu respuesta: ")#Se toma la respuesta

        if respuesta == "s":#Si la respuesta es afirmativa toma este camino
            
            rutaOrigen=input("\nIngrese la ruta de la imagen que desea convertir: ")#Se captura la ruta de la imagen a convertir
            


            rutaOrigenDividida=rutaOrigen.split(".")#La ruta se divide a partir del "."
            rutaSinExtension=rutaOrigenDividida[0]#ruta sin extension de archivo seleccionado
            ext=rutaOrigenDividida[-1]#extension de archivo seleccionado

            print("La extension de la imagen seleccionada es  ."+ext+"\n")#Imprime la extension del archivo        
            
                     
            #En base al tipo de extension se mostraran los tipos de formato a los que puede convertir ↓↓↓
            
            if ext == "jpg":
                print("Puede seleccionar una de las siguientes opciones para convertir \n 1.png \n 2.gif \n 3.bmp \n")#Se imprime pregunta de opciones a convertir
                n=input("Ingrese el numero: ")#Se toma el valor
                if n.isdigit():#Se verifica si el valor de la cadena es un numero
                    numero=int(n)#Si es un numero se convierte a entero
                    #En base al numero ingresado se ejecutara el metodo ↓↓↓
                    if numero == 1:
                        self.convertirApng(rutaOrigen,rutaSinExtension)
                        
                    elif numero == 2:
                        self.convertirAgif(rutaOrigen,rutaSinExtension)
                        
                    elif numero == 3:
                        self.convertirAbmp(rutaOrigen,rutaSinExtension)         
                    else:
                        print("\nPor favor lea atentamente e ingrese alguna de las opciones segun corresponda.")
                        c.convertirImagen()#Si el numero ingresado no esta en las opciones se inica el programa nuevamente
                else:
                        print("\nPor favor lea atentamente e ingrese alguna de las opciones segun corresponda.")
                        c.convertirImagen()#Si el valor no es un numero se inica el programa nuevamente

            elif ext == "png":
                print("Puede seleccionar una de las siguientes opciones para convertir \n 1.jpg \n 2.gif \n 3.bmp \n")
                n=input("Ingrese el numero: ")
                if n.isdigit():
                    numero=int(n)
                    if numero == 1:
                        self.convertirAjpg(rutaOrigen,rutaSinExtension)
                        
                    elif numero == 2:
                        self.convertirAgif(rutaOrigen,rutaSinExtension)
                        
                    elif numero == 3:
                        self.convertirAbmp(rutaOrigen,rutaSinExtension)
                    else:
                        print("\nPor favor lea atentamente e ingrese alguna de las opciones segun corresponda.")
                        c.convertirImagen()
                else:
                        print("\nPor favor lea atentamente e ingrese alguna de las opciones segun corresponda.")
                        c.convertirImagen()    
                    
            elif ext == "gif":
                print("Puede seleccionar una de las siguientes opciones para convertir \n 1.jpg \n 2.png \n 3.bmp \n")
                n=input("Ingrese el numero: ")
                if n.isdigit():
                    numero=int(n)
                    if numero == 1:
                        self.convertirAjpg(rutaOrigen,rutaSinExtension)
                        
                    elif numero == 2:
                        self.convertirApng(rutaOrigen,rutaSinExtension)
                        
                    elif numero == 3:
                        self.convertirAbmp(rutaOrigen,rutaSinExtension)
                    else:
                        print("\nPor favor lea atentamente e ingrese alguna de las opciones segun corresponda.")
                        c.convertirImagen()
                else:
                        print("\nPor favor lea atentamente e ingrese alguna de las opciones segun corresponda.")
                        c.convertirImagen()
                        
            elif ext == "bmp":
                print("Puede seleccionar una de las siguientes opciones para convertir \n 1.jpg \n 2.png \n 3.gif \n")
                n=input("Ingrese el numero: ")
                if n.isdigit():
                    numero=int(n)
                    if numero == 1:
                        self.convertirAjpg(rutaOrigen,rutaSinExtension)
                        
                    elif numero == 2:
                        self.convertirApng(rutaOrigen,rutaSinExtension)
                        
                    elif numero == 3:
                        self.convertirAgif(rutaOrigen,rutaSinExtension)
                    else:
                        print("\nPor favor lea atentamente e ingrese alguna de las opciones segun corresponda.")
                        c.convertirImagen()
                else:
                        print("\nPor favor lea atentamente e ingrese alguna de las opciones segun corresponda.")
                        c.convertirImagen()
                        
            else:
                print("Formato de imagen no valido recuerde que la imagen debe ser .jpg /.png /.gif o .bmp \n")
                c.convertirImagen()#Si la extension del formato no coincide con alguna de las opciones se inica el programa nuevamente

            c.convertirImagen()#Inica el programa nuevamente

        elif respuesta == "n":#Si la respuesta es negativa toma este camino
            sys.exit()
             

        else:
            print("\nPor favor lea atentamente e ingrese alguna de las opciones segun corresponda.")
            c.convertirImagen()#Si el valor ingresado no corresponde a las opciones se inica el programa nuevamente
            
            

