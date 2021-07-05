from tkinter import Tk, PhotoImage, Label
from glob import glob
from itertools import cycle

# this method calls itself again after 1000 milliseconds
def show_next():
    image.configure(file=next(images))
    root.after(1000, show_next)

# cycle though png images found in working directory
images = cycle(glob("images/imagenes/*.png"))

# build minimal test GUI
root = Tk()
image = PhotoImage()
Label(root, image=image).pack()

# start slide show and GUI main loop
show_next()
root.mainloop()