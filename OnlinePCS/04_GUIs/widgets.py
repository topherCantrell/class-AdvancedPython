import Tkinter
import ttk

top = Tkinter.Tk()

# This object is shared by the widget and your own code
s = Tkinter.IntVar()
s.set(10)

#cb = ttk.Checkbutton(top, text="Click on me", variable=s)
#cb.pack()


rb1 = ttk.Radiobutton(top, text="Penny", variable=s, value=1)
rb1.pack()
rb2 = ttk.Radiobutton(top, text="Nickel", variable=s, value=5)
rb2.pack()
rb3 = ttk.Radiobutton(top, text="Dime", variable=s, value=10)
rb3.pack()
rb4 = ttk.Radiobutton(top, text="Quarter", variable=s, value=25)
rb4.pack()


def ontest():
    print "hello!"

menubar = Tkinter.Menu(top)

filemenu = Tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=ontest)
filemenu.add_command(label="Save", command=ontest)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Tkinter.Menu(menubar, tearoff=1)
editmenu.add_command(label="Cut", command=ontest)
editmenu.add_command(label="Copy", command=ontest)
editmenu.add_command(label="Paste", command=ontest)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=ontest)
menubar.add_cascade(label="Help", menu=helpmenu)

top.config(menu=menubar)

top.mainloop()

print "HELLO FROM HERE"