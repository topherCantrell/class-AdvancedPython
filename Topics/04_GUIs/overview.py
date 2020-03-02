import Tkinter
import ttk

def onClick():
    print("I am here")
    print("From:"+c1.get())
    print("To:"+c2.get())
    print("Value:"+inp.get())
    his.configure(state="normal")
    his.insert(Tkinter.END,"\nHELLO")
    his.configure(state="disabled")

top = Tkinter.Tk()

m1 = ttk.Label(top, text="Convert")
m1.pack()

c1 = ttk.Combobox(top, values=["inches","feet","cm","mm"])
c1.set("inches")
c1.pack()

m2 = ttk.Label(top, text="to")
m2.pack()

c2 = ttk.Combobox(top, values=["inches","feet","cm","mm"])
c2.set("cm")
c2.pack()

m3 = ttk.Label(top, text="Value")
m3.pack()

inp = ttk.Entry(top)
inp.pack()

c = ttk.Checkbutton(top,text="Testing")
c.pack()

bt = ttk.Button(top, text="Convert",command=onClick)
bt.pack()

his = Tkinter.Text(top, height=8, width=30)
his.insert(Tkinter.END,"5 inches = 20 miles")
his.configure(state="disabled")
his.pack()

top.mainloop()