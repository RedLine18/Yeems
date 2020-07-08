from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)

global hairValue
global imagePath

def choose_left():
    hairValue-=1

def choose_right():
    hairValue+=1

def determine_img():
    hairValue = 1
    if hairValue == 1:
        imagePath = "../Resources/Untitled.png"
    return imagePath


if __name__ == '__main__':
    x = determine_img()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()

btn = Button(root, text='Generate', command=determine_img()).pack()

root.mainloop()
