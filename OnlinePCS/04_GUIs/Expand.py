import Tkinter

top = Tkinter.Tk()

listbox = Tkinter.Listbox(top)
for i in range(20):
    listbox.insert(Tkinter.END, str(i))
listbox.pack( expand=1)

listbox2 = Tkinter.Listbox(top)
for i in range(20):
    listbox2.insert(Tkinter.END, str(i))
listbox2.pack(expand=1)

top.mainloop()
