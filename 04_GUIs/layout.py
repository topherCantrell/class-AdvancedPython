import Tkinter

root = Tkinter.Tk()

top = Tkinter.Frame(root,bg="blue")
bottom = Tkinter.Frame(root,bg="green")

top.pack(expand=1,fill=Tkinter.BOTH)
bottom.pack(expand=1,fill=Tkinter.BOTH)


m1 = Tkinter.Label(top,text="A");
m2 = Tkinter.Label(top,text="B");
m3 = Tkinter.Label(top,text="C");
m4 = Tkinter.Label(top,text="D");

m1.grid(row=0,column=0)
m2.grid(row=0,column=1)
m3.grid(row=1,column=0)
m4.grid(row=1,column=1)

"""
b1 = Tkinter.Button(bottom,text="OK")
b2 = Tkinter.Button(bottom,text="Cancel")

b1.pack(anchor=Tkinter.CENTER,expand=1)
b2.pack(anchor=Tkinter.SE,expand=1)
"""

root.mainloop()
