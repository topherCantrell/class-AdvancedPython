import tkinter
from tkinter import ttk

TO_MM = {
    'inches' : 25.4,
    'feet'   : 25.4 * 12,
    'cm'     : 10,
    'mm'     : 1
}

def onClick():
    from_units = c1.get()
    to_units = c2.get()
    value = inp.get()
    
    value = float(value)
    old_value = value
    
    value = value * TO_MM[from_units]
    value = value / TO_MM[to_units]
           
    his.configure(state="normal")
    his.insert(tkinter.END,'\n{} {} is {} {}'.format(old_value,from_units,value,to_units))
    his.configure(state="disabled")

top = tkinter.Tk()
m1 = ttk.Label(top, text="Convert")
c1 = ttk.Combobox(top, values=["inches","feet","cm","mm"])
c1.set("inches")
m2 = ttk.Label(top, text="to")
c2 = ttk.Combobox(top, values=["inches","feet","cm","mm"])
c2.set("cm")
m3 = ttk.Label(top, text="Value")
inp = ttk.Entry(top)
bt = ttk.Button(top, text="Convert",command=onClick)
his = tkinter.Text(top, height=8, width=30)
his.configure(state="disabled")

m1.pack()
c1.pack()
m2.pack()
c2.pack()
m3.pack()
inp.pack()
bt.pack()
his.pack()

top.mainloop()