from tkinter import *
from tkinter import colorchooser
from PIL import ImageTk,Image

def change_img_colour(img, colour, pal_size=64):
    index_img = img.convert('RGBA').convert(mode='P', dither='NONE', colors = pal_size)
    palette = index_img.getpalette()
    for i in range(pal_size):
        i = i * 3

        r_index = i
        g_index = i+1
        b_index = i+2

        palette[r_index] = int(palette[r_index] - (palette[r_index] - colour[0])/2)
        palette[g_index] = int(palette[g_index] - (palette[g_index] - colour[1])/2)
        palette[b_index] = int(palette[b_index] - (palette[b_index] - colour[2])/2)
    index_img.putpalette(palette)
    return index_img

root = Tk()

img = ImageTk.PhotoImage(Image.open("../Resources/Untitled.png"))

def colour_wolour():
    global img
    clr = colorchooser.askcolor(title="color wolour")
    img = ImageTk.PhotoImage(change_img_colour(Image.open("../Resources/Untitled.png"), clr[0]))

change_colour = Button(root, text="Change colour", command=colour_wolour)
change_colour.pack()

canvas = Canvas(root, width = 1000, height = 1000)
canvas.pack()


while True:
    canvas.create_image(20, 20, anchor=NW, image=img)
    root.update()
    root.update_idletasks()