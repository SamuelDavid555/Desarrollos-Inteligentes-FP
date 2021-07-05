
import speech_recognition as sr
# Se inicializa el reconocedor
r = sr.Recognizer()

# Se importan las librerias a utilizar
from tkinter import Tk, PhotoImage, Label, Text, INSERT
from glob import glob
from itertools import cycle

# Se crea la interfaz en donde iran las imagenes
root = Tk()
root.title("Traductor de voz a lengua de señas")
root.geometry("720x500")



# Cambia los acentos por letras sin acento para evitar problemas localizando
# la imagen correspondiente
def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

# Carga la siguiente imagen y la cambia dentro de la interfaz
def show_next():
    # Obtiene la siguiente imagen de la lista deimagenes
    currentImage = next(images)
    # De la ruta obtiene el nombre de la palabra
    currentImageElements = currentImage.split('/')
    # Agarra el utlimo elemento de la lista y elimina su extension
    imageName = currentImageElements[-1][0:-4]
    
    # Obtiene el elemento label de root para cambiar el nombre de la palabra
    labels = root.winfo_children()
    labels[0].configure(text=imageName)
    
    # Cambia la imagen en la interfaz y duerme por 1s para mostrar la sig
    image.configure(file=currentImage)
    root.after(1000, show_next)

# Empezamos el metodo para reconocer el texto
with sr.Microphone() as source:
    # Imprimirmos en pantalla y empezamos a escuchar al dispositivo de audio
    print("Di algo...")
    audio = r.listen(source)

    try:
        # De google tratamos de reconocer el audio en español
        text = r.recognize_google(audio, language='es-ES')
        palabra = "{}".format(text)
        # Formateamos el texto y lo mostramos en pantalla
        print("Tu dijiste: {}".format(text))
        
        # Normalizamos todas las palabras para dejarlas sin acentos
        palabra = normalize(palabra)
        # Separamos las palabras y las convertimos a rutas de imagen
        resSplit = palabra.split()
        for index, word in enumerate(resSplit):
            resSplit[index] = 'images/{}.png'.format(word) 

        # Imprimimos las rutas
        print(resSplit)

        # Creamos el objeto imagen para mostrarlo en pantalla
        image = PhotoImage()
        image = image.zoom(25)
        image = image.subsample(32) 
        lbl = Label(root, text="", image=image, compound='bottom', font=('Helvatical bold',20)).pack()
       
        # Empezamos el ciclo de las imagenes y cargamos la interfaz
        images = cycle(resSplit)
        show_next()
        root.mainloop()

    # Maneja la excepcion
    except Exception as e:
        print(e)
        print("Perdon pero no entiendo")
        pass
        

