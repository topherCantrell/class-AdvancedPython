import tkinter
from tkinter import ttk

top = tkinter.Tk()

messages = tkinter.Text(top, height=10, width=40)
messages.pack()

lab_show = ttk.Label(top,text="Show from")
lab_show.pack()

text_from = ttk.Entry(top)
text_from.pack()

bt_refresh = ttk.Button(top,text="Refresh")
bt_refresh.pack()

bt_refresh = ttk.Button(top,text="Clear")
bt_refresh.pack()

lab_sender = ttk.Label(top,text="Sender")
lab_sender.pack()

text_sender = ttk.Entry(top)
text_sender.pack()

lab_message = ttk.Label(top,text="Message")
lab_message.pack()

text_message = ttk.Entry(top)
text_message.pack()

bt_post = ttk.Button(top,text="Post")
bt_post.pack()

top.mainloop()