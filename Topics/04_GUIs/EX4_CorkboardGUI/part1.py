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
    messages.configure(state="normal")
    messages.delete('1.0', tkinter.END)    
    for ms in board.get_messages():
        messages.insert(tkinter.END,str(ms)+"\n")
    messages.configure(state="disabled")
    
def clear():
    board.clear()
    refresh()

top = tkinter.Tk()

messages = tkinter.Text(top, height=10, width=70)
messages.pack()

lab_show = ttk.Label(top,text="Show from")
lab_show.pack()

text_from = ttk.Entry(top)
text_from.pack()

bt_refresh = ttk.Button(top,text="Refresh",command=refresh)
bt_refresh.pack()

bt_clear = ttk.Button(top,text="Clear",command=clear)
bt_clear.pack()

lab_sender = ttk.Label(top,text="Sender")
lab_sender.pack()

text_sender = ttk.Entry(top)
text_sender.pack()

lab_message = ttk.Label(top,text="Message")
lab_message.pack()

text_message = ttk.Entry(top)
text_message.pack()

bt_post = ttk.Button(top,text="Post",command=post_message)
bt_post.pack()

top.mainloop()