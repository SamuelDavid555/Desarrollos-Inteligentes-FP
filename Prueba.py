import speech_recognition as sr

r = sr.Recognizer()


from tkinter import Tk, PhotoImage, Label, Text, INSERT
from glob import glob
from itertools import cycle

root = Tk()
root.title("Traductor de voz a lengua de señas")

root.geometry("720x360")




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


def show_next():
    currentImage = next(images)
    currentImageElements = currentImage.split('/')
    imageName = currentImageElements[-1][0:-4]
    
    labels = root.winfo_children()
    labels[0].configure(text=imageName)
    
    image.configure(file=currentImage)
    root.after(1000, show_next)

with sr.Microphone() as source:
    print("Di algo...")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='es-ES')
        palabra = "{}".format(text)
        print("Tu dijiste: {}".format(text))
        
        palabra = normalize(palabra)
        resSplit = palabra.split()
        for index, word in enumerate(resSplit):
            resSplit[index] = 'images/{}.png'.format(word) 

        print(resSplit)

       
        image = PhotoImage()
        image = image.zoom(25)
        image = image.subsample(32) 
        lbl = Label(root, text="d", image=image, compound='bottom', font=('Helvatical bold',20)).pack()
       
        # start slide show and GUI main loop
        images = cycle(resSplit)
        show_next()
        root.mainloop()

    except Exception as e:
        print(e)
        print("Perdon pero no entiendo")
        

