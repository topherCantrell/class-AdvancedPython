import tkinter
from tkinter import ttk

import corkboard

board = corkboard.CorkBoard()
corkboard.make_example_data(board)

def post_message():
    print("POST MESSAGE")
    mes = corkboard.Message(text_sender.get(),text_message.get(),"TODO NOW")
    board.post_message(mes)    
    refresh()
    
def refresh():
    senders = text_from.get().split(',')   
    messages.configure(state="normal")
    messages.delete('1.0', tkinter.END)    
    for ms in board.get_messages_from(senders):
        messages.insert(tkinter.END,str(ms)+"\n")
    messages.configure(state="disabled")
    
def clear():
    board.clear()
    refresh()

top = tkinter.Tk()

messages = tkinter.Text(top, height=10, width=70)
messages.pack(fill=tkinter.BOTH,expand=1)

row1 = tkinter.Frame(top)

lab_show = ttk.Label(row1,text="Show from",width=10,anchor=tkinter.E)

lab_show.pack(side=tkinter.LEFT)

text_from = ttk.Entry(row1)
text_from.pack(side=tkinter.LEFT,fill=tkinter.X,expand=1)

bt_clear = ttk.Button(row1,text="Clear",command=clear)
bt_clear.pack(side=tkinter.RIGHT)

bt_refresh = ttk.Button(row1,text="Refresh",command=refresh)
bt_refresh.pack(side=tkinter.RIGHT)

row1.pack(fill=tkinter.X)

row2 = tkinter.Frame(top)

lab_sender = ttk.Label(row2,text="Sender",width=10,anchor=tkinter.E)
lab_sender.pack(side=tkinter.LEFT)

text_sender = ttk.Entry(row2)
text_sender.pack(side=tkinter.LEFT)

lab_message = ttk.Label(row2,text="Message")
lab_message.pack(side=tkinter.LEFT)

text_message = ttk.Entry(row2)
text_message.pack(side=tkinter.LEFT,fill=tkinter.X,expand=1)

bt_post = ttk.Button(row2,text="Post",command=post_message)
bt_post.pack(side=tkinter.LEFT)

row2.pack(fill=tkinter.X)

refresh()

top.mainloop()