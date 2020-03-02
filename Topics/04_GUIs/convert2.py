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

root = tkinter.Tk()

root.configure(background='blue')

top = tkinter.Frame(root)
m1 = ttk.Label(top, text="Convert")
c1 = ttk.Combobox(top, values=["inches","feet","cm","mm"])
c1.set("inches")
m2 = ttk.Label(top, text="to")
c2 = ttk.Combobox(top, values=["inches","feet","cm","mm"])
c2.set("cm")
m3 = ttk.Label(top, text="Value")
inp = ttk.Entry(top)
bt = ttk.Button(top, text="Convert",command=onClick)
m1.grid(row=0,column=0)
c1.grid(row=0,column=1)
m2.grid(row=1,column=0)
c2.grid(row=1,column=1)
m3.grid(row=2,column=0)
inp.grid(row=2,column=1)
bt.grid(row=3,column=0)



his = tkinter.Text(root, height=8, width=30)
his.configure(state="disabled")

top.pack()
his.pack(expand=1,fill=tkinter.BOTH)

top.mainloop()