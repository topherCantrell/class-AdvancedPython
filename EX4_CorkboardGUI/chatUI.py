import Tkinter
import ttk
import CorkBoard
import Message

def clear():
    board.clear()
    refresh()
    # print "CLEAR"

def refresh():    
    s = fil.get().replace(" ","")
    filt = []
    if len(s)>0:
        filt = s.split(",")
    #print "REFRESH :"+str(filt)+":"
    messages = board.getMessagesFrom(filt)
    log.configure(state="normal")
    log.delete(1.0,Tkinter.END)
    for m in messages:
        log.insert(Tkinter.END,str(m)+"\n")
    log.configure(state="disabled")

def postMessage():
    message = Message.Message(snd.get(),msg.get())
    board.postMessage(message)
    #print "POST :"+snd.get()+":"+msg.get()+":"

board = CorkBoard.CorkBoard()
CorkBoard.makeExampleData(board)

root = Tkinter.Tk()

root.title("Message")
root.iconbitmap("chat.ico")

log = Tkinter.Text(root, height=20, width=80)
log.configure(state="disabled")

cntrls = Tkinter.Frame(root)

filLabel = ttk.Label(cntrls, text="Filter:")
fil = ttk.Entry(cntrls)
btClr = ttk.Button(cntrls,text="Clear",command=clear)
btRefresh = ttk.Button(cntrls,text="Refresh",command=refresh)

msgentry = Tkinter.Frame(root)

sndLabel = ttk.Label(msgentry,text="Sender:")
msg = ttk.Entry(msgentry)
blnk = ttk.Label(msgentry,text="    ")
msgLabel = ttk.Label(msgentry,text="Message:")
snd = ttk.Entry(msgentry)
btPost = ttk.Button(msgentry,text="Post", command=postMessage)

log.pack()

filLabel.pack(side=Tkinter.LEFT)
fil.pack(side=Tkinter.LEFT)
btClr.pack(side=Tkinter.RIGHT)
btRefresh.pack(side=Tkinter.RIGHT)

cntrls.pack(expand=1,fill=Tkinter.X)

sndLabel.pack(side=Tkinter.LEFT)
snd.pack(side=Tkinter.LEFT)
blnk.pack(side=Tkinter.LEFT)
msgLabel.pack(side=Tkinter.LEFT)
msg.pack(side=Tkinter.LEFT)
btPost.pack(side=Tkinter.LEFT)
msgentry.pack(side=Tkinter.LEFT,pady=10,padx=40)

refresh()

root.mainloop()

