import Tkinter

root = Tkinter.Tk()


root.title("HiLo")
root.iconbitmap("hilo.ico")

ins1 = Tkinter.Label(root,text="I am thinking of a number between 1 and 100.", anchor=Tkinter.W)
ins2 = Tkinter.Label(root,text="You guess it!", anchor=Tkinter.W)

gb = Tkinter.Frame(root)
bp = Tkinter.Frame(root)

lab = Tkinter.Label(gb,text="Guess:")
inp = Tkinter.Entry(gb)
hint = Tkinter.Label(gb,text="Higher!");

bt1 = Tkinter.Button(bp,text="OK")
bt2 = Tkinter.Button(bp,text="New Game")

ins1.pack(fill=Tkinter.X)
ins2.pack(fill=Tkinter.X)

lab.grid(row=0,column=0)
inp.grid(row=0,column=1)
hint.grid(row=0,column=2)

bt1.pack(side=Tkinter.LEFT)
bt2.pack()

gb.pack(anchor=Tkinter.W)
bp.pack()



root.mainloop()