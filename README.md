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
        c=Conversor()                                         Instancia de la clase.
        print("\n¿Desea convertir alguna imagen ?")           Se imprime pregunta  .
        print("Presione s para si")                           Se imprimen opciones.
        print("Presione n para no\n")

        respuesta=input("Escribe tu respuesta: ")            Se toma la respuesta que puede ser la letra "s" o la "n".
        if respuesta == "s":                                 Si la respuesta es afirmativa toma este camino.
            
            rutaOrigen=input("\nIngrese la ruta de la imagen que desea convertir: ")      Se captura la ruta de la imagen a convertir.
            


            rutaOrigenDividida=rutaOrigen.split(".")                       La ruta se divide a partir del "."
            rutaSinExtension=rutaOrigenDividida[0]                         ruta sin extension de archivo seleccionado.
            ext=rutaOrigenDividida[-1]                                     Extension de archivo seleccionado.
    
            print("La extension de la imagen seleccionada es  ."+ext+"\n")                Imprime la extension del archivo seleccionado.
            
            
            
            
**En base al tipo de extension se mostraran los tipos de formato a los que puede convertir ↓↓↓**

   Si el tipo de archivo a convertir su extención Jpg, en el siguiente metodo muestra las opciones que tiene para convertir, diferentes a la que ya tiene.
            
            if ext == "jpg":
                print("Puede seleccionar la siguientes opciones a convertir \n 1.png \n 2.gif \n 3.bmp \n")       Se imprime la pregunta con las opciones a convertir
                n=input("Ingrese el numero: ")                                                                    Se toma el valor ingresado.
                if n.isdigit():                                                                                   Se verifica si el valor de la cadena es un número.
                    numero=int(n)                                                                                 Si es un número se convierte a entero.
                    
   En base al numero ingresado se ejecutara el metodo ↓↓↓
   
                    if numero == 1:
                        self.convertirApng(rutaOrigen,rutaSinExtension)
                        
                    elif numero == 2:
                        self.convertirAgif(rutaOrigen,rutaSinExtension)
                        
                    elif numero == 3:
                        self.convertirAbmp(rutaOrigen,rutaSinExtension)         
                    else:
                        print("\nPor favor lea atentamente e ingrese alguna de las opciones segun corresponda.")
                        c.convertirImagen()                                        Si el numero ingresado no esta en las opciones se inica el programa nuevamente.
                else:
                        print("\nPor favor lea atentamente e ingrese alguna de las opciones segun corresponda.")
                        c.convertirImagen()                                        Si el valor no es un numero se inica el programa nuevamente.
                        

Si el tipo de archivo a convertir su extención PNG, en el siguiente metodo muestra las opciones que tiene para convertir, diferentes a la que ya tiene.

            elif ext == "png":
                print("Puede seleccionar la siguientes opciones a convertir \n 1.jpg \n 2.gif \n 3.bmp \n")
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
                        
                        
Si el tipo de archivo a convertir su extención GIF, en el siguiente metodo muestra las opciones que tiene para convertir, diferentes a la que ya tiene.}


            elif ext == "gif":
                print("Puede seleccionar la siguientes opciones a convertir \n 1.jpg \n 2.png \n 3.bmp \n")
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
                        
                        
Si el tipo de archivo a convertir su extención BMP, en el siguiente metodo muestra las opciones que tiene para convertir, diferentes a la que ya tiene.
                        
            elif ext == "bmp":
                print("Puede seleccionar la siguientes opciones a convertir \n 1.jpg \n 2.png \n 3.gif \n")
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

            c.convertirImagen()                    Inica el programa nuevamente

        elif respuesta == "n":                     Si la respuesta es negativa toma este camino
            sys.exit()
             

        else:
            print("\nPor favor lea atentamente e ingrese alguna de las opciones segun corresponda.")
            c.convertirImagen()                    Si el valor ingresado no corresponde a las opciones se inica el programa nuevamente
            
            
            
            
            
* **Ejecutable desde Sistema Operativo Linux. Aplicación creada por consola**


1. Una vez hayamos creado nuestro ejecutable a travez de Paint Select, este nos creará unas carpetas llamadas **"build", "dist" y "pycache"*


![image](https://user-images.githubusercontent.com/44372737/110686241-3c8b0080-81ad-11eb-9ec1-d0f528524c99.png)
![image](https://user-images.githubusercontent.com/44372737/110686297-4a408600-81ad-11eb-98a5-8cb144bed394.png)
![image](https://user-images.githubusercontent.com/44372737/110686335-50cefd80-81ad-11eb-804a-c189fc1b29b2.png)

2. En este caso nos interesa saber que hay en el contenido de la carpeta llamada "dist", ya que ahí se encuentra almacenado nuestro ejecutable.
Dentro de ella habrá una carpeta llamana **"main"**;

![image](https://user-images.githubusercontent.com/44372737/110686866-e5396000-81ad-11eb-8868-9f251c670080.png)

3. Una vez ingresado a la carpeta "main", buscamos un archivo llamado "main" que es nuestro ejecutable.

![image](https://user-images.githubusercontent.com/44372737/110687197-42351600-81ae-11eb-9eda-be4dc1bd9494.png)

4. Vamos a Abrirlo por medio de la terminar, damos clic derecho por fuera de la carpeta y seleccionamos la opción que dice **"Abrir en una terminal"**

![image](https://user-images.githubusercontent.com/44372737/110687608-afe14200-81ae-11eb-99e4-8d6486accf32.png)
![image](https://user-images.githubusercontent.com/44372737/110687811-eae37580-81ae-11eb-8772-fa47a80796d4.png)

Abrimos la terminal dentro de esta carpeta para situarnos en ella y para ejecutar ya que es un archivo .bash

5. Escribimos en la terminal lo siguiente **"./"** y el nombre del archivo que en este caso de llama **"main"**

![image](https://user-images.githubusercontent.com/44372737/110688562-b3c19400-81af-11eb-976a-f07551b2c71a.png)

6. De esta manera se imprimirá en pantalla el programa en ejecución

![image](https://user-images.githubusercontent.com/44372737/110688886-10bd4a00-81b0-11eb-8f9f-09007fdea468.png)

7. En adelante se comenzará a mostrar el funcionamiento del aplicativo en consola.
   
   La aplicación comienza haciendo una pregunta la cuál dice "Desea convertir alguna imagen", la cual tiene como opciones de respuesta: "S" para decir si, o "n" para decir no. 
   Se contesta con la S para seguir explicando su funcionamiento. 
   
   ![image](https://user-images.githubusercontent.com/44372737/110690027-6b0ada80-81b1-11eb-825c-5720c158d72d.png)
   
8. Ahora debes ingresar la ruta de la imagen a convertir. Para realizar esa accion, te debes dirigir donde está la imagen que quieres convertir, das clic derecho por fuera de la imagen y seleccionas la opción **"Abrir en una terminal"**

![image](https://user-images.githubusercontent.com/44372737/110690992-9215dc00-81b2-11eb-822f-20efb5ab9e3f.png)

![image](https://user-images.githubusercontent.com/44372737/110690686-39464380-81b2-11eb-9266-d1f10d1b7b44.png)

9. Escribimos el siguiente comando junto con el nombre de la imagen, en este caso la imagen del ejemplo se llama **"firma.png"**

![image](https://user-images.githubusercontent.com/44372737/110691134-bec9f380-81b2-11eb-8890-2554c5d873ae.png)

10. Con ese comando nos devuelve la ruta de la imagen. 

![image](https://user-images.githubusercontent.com/44372737/110691393-15cfc880-81b3-11eb-98d2-7b874c4cd70a.png)

11. La seleccionamos y copiamos.

![image](https://user-images.githubusercontent.com/44372737/110691543-457ed080-81b3-11eb-842e-c82c5b261c23.png)

12. Nos dirigimos a la terminar donde se está ejecutando nuestra aplicación por consola y la pegamos.

![image](https://user-images.githubusercontent.com/44372737/110691760-8aa30280-81b3-11eb-87ca-b04dd457dca6.png)

13. La aplicación lee y muestra la extención de la imagen, que en este caso es **".png"**. 
    Tambien muestra las opciones a las cuales la puedo convertir, diferentes al de la imagen. 
    
    1. "jpg"
    2. "gif"
    3. "bmp"

![image](https://user-images.githubusercontent.com/44372737/110692207-1ae14780-81b4-11eb-8fb1-a07cff3202d6.png)

14. Para el ejemplo se va a convertir en .jpg la cual es la opción 1.

![image](https://user-images.githubusercontent.com/44372737/110692325-43694180-81b4-11eb-905f-2c50d852e5d5.png)

![image](https://user-images.githubusercontent.com/44372737/110692452-5419b780-81b4-11eb-847e-3b118a59aea6.png)

15. ¡Listo!, ahora nos dirigimos a la carpeta donde buscamos la imagen y junto a ella debe estar la nueva imagen creada, con la extención convertida.

![image](https://user-images.githubusercontent.com/44372737/110692742-ae1a7d00-81b4-11eb-97b8-9a0a04e4fa08.png)

![image](https://user-images.githubusercontent.com/44372737/110692769-b8d51200-81b4-11eb-958d-a5eed6d66b4f.png)

16. Ya hecha la conversión, la aplicación se reinicia para volverla a ejecutar y convertir otra imagen de nuevo. 

![image](https://user-images.githubusercontent.com/44372737/110693210-300aa600-81b5-11eb-8a97-c8e0817357b4.png)
