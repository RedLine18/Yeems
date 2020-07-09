import tkinter as tk
from tkinter import *
from tkinter import colorchooser
import itertools
from PIL import ImageTk, Image

win = tk.Tk()
win.geometry('800x1000')
win.resizable(0, 0)

canvas = Canvas(win, width=800, height=800)
canvas.pack()

img_index = 0

img_paths = ["../Resources/Untitled.png", "../Resources/Human Male 1.png"]
imgs = []
for i in img_paths:
    imgs.append(ImageTk.PhotoImage(Image.open(i)))


def next_img():
    global img_index
    img_index = img_index + 1
    if img_index > len(img_paths) - 1:
        img_index = 0
    img = ImageTk.PhotoImage(Image.open(img_paths[img_index]))


def change_img_colour(img, colour, pal_size=64):
    index_img = img.convert('RGBA').convert(mode='P', dither='NONE', colors=pal_size)
    palette = index_img.getpalette()
    for i in range(pal_size):
        i = i * 3

        r_index = i
        g_index = i + 1
        b_index = i + 2

        palette[r_index] = int(palette[r_index] - (palette[r_index] - colour[0]) / 2)
        palette[g_index] = int(palette[g_index] - (palette[g_index] - colour[1]) / 2)
        palette[b_index] = int(palette[b_index] - (palette[b_index] - colour[2]) / 2)
    index_img.putpalette(palette)
    return index_img


def colour_wolour():
    clr = colorchooser.askcolor(title="color wolour")
    imgs[img_index] = ImageTk.PhotoImage(change_img_colour(Image.open(img_paths[img_index]), clr[0]))


change_colour = Button(text="Change colour", command=colour_wolour)
change_colour.pack()
nextImageButton = tk.Button(text='Next image', command=next_img).place(x=10, y=10)

next_img()

while True:
    for i in imgs:
        canvas.create_image(50, 100, anchor=NW, image=i)

    win.update()
    win.update_idletasks()
