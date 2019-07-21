from tkinter import *

def make_gui():
    global canvas
    master = Tk()
    canvas = Canvas(master, width=500, height=400)
    canvas.pack()
    return canvas

def make_rectangle(x,y):
    global canvas
    id = canvas.create_rectangle(x,y,x+20,y+20)
    return id

def move(id,xofs,yofs):
    global canvas
    canvas.move(id,xofs,yofs)

def run_gui():
    mainloop()