import tkinter as tk
from tkinter import *
from tkinter import colorchooser
import itertools
from PIL import ImageTk, Image

win = tk.Tk()
win.geometry('800x900')
win.resizable(0, 0)

canvas = Canvas(win, width=500, height=500)
canvas.pack()

img_index = 0

img_paths = ["../Resources/hair1.png", "../Resources/base1.png", "../Resources/eyebrows1.png", "../Resources/eyes1.png",
             "../Resources/nose1.png", "../Resources/mouth1.png"]

color = []
for i in img_paths:
    color.append([0, 0, 0])

slot_options = [1, 1, 1, 1, 1, 1, 1]

vhair = 0
vhead_shape = 1
veyebrows = 2
veyes = 3
vnose = 4
vmouth = 5
vfacial_acc = 6

slots = [["../Resources/hair1.png"], ["../Resources/base1.png"],
         ["../Resources/eyebrows1.png"], ["../Resources/eyes1.png"], ["../Resources/nose1.png"],
         ["../Resources/mouth1.png"]]

imgs = []
for i in img_paths:
    imgs.append(ImageTk.PhotoImage(Image.open(i)))


def hair():
    global img_index
    img_index = vhair


def head_shape():
    global img_index
    img_index = vhead_shape


def eyebrows():
    global img_index
    img_index = veyebrows


def eyes():
    global img_index
    img_index = veyes


def nose():
    global img_index
    img_index = vnose


def mouth():
    global img_index
    img_index = vmouth


def facial_acc():
    global img_index
    img_index = vfacial_acc


def next_option():
    global slot_options
    slot_options[img_index] = slot_options[img_index] + 1
    if slot_options[img_index] > len(slots[img_index]) - 1:
        slot_options[img_index] = 0
    img_paths[img_index] = slots[img_index][slot_options[img_index]]
    imgs[img_index] = ImageTk.PhotoImage(Image.open(img_paths[img_index]))


def prev_option():
    global slot_options
    slot_options[img_index] = slot_options[img_index] - 1
    if slot_options[img_index] < 0:
        slot_options[img_index] = len(slots[img_index]) - 1
    img_paths[img_index] = slots[img_index][slot_options[img_index]]
    imgs[img_index] = ImageTk.PhotoImage(Image.open(img_paths[img_index]))

    imgs[img_index] = ImageTk.PhotoImage(change_img_colour(Image.open(img_paths[img_index]), color[img_index]))


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
    color[img_index] = clr[0]


change_colour = Button(text="Change colour", command=colour_wolour)
change_colour.pack()

changeSlotButton = tk.Button(text='Next option', command=next_option).place(x=10, y=50)
prevSlotButton = tk.Button(text="Prev option", command=prev_option).place(x=685, y=50)
hairButton = tk.Button(text="Hair", command=hair).place(x=10, y=100)
headButton = tk.Button(text="Head", command=head_shape).place(x=10, y=150)
eyebrowButton = tk.Button(text="Eyebrow", command=eyebrows).place(x=10, y=200)
eyesButton = tk.Button(text="Eyes", command=eyes).place(x=10, y=250)
noseButton = tk.Button(text="Nose", command=nose).place(x=10, y=300)
mouthButton = tk.Button(text="Mouth", command=mouth).place(x=10, y=350)
facialaccButton = tk.Button(text="Facial Accessories", command=facial_acc).place(x=10, y=400)
next_option()

while True:
    for i in imgs:
        
        canvas.create_image(50, 100, anchor=NW, image=i)

    win.update()
    win.update_idletasks()
