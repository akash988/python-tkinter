#frames
from tkinter import *
root=Tk()
root.geometry("655x333")

f1=Frame(root,bg="gray",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)
f2=Frame(root,bg="gray",borderwidth=6,relief=SUNKEN)
f2.pack(side=TOP,fill=X)

l=Label(f1,text="Project Tkinter")
l.pack()
l1=Label(f2,text="Welcome To Window")
l1.pack()


root.mainloop()