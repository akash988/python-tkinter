from tkinter import *
root=Tk()
root.geometry("655x333")

def name():
    print("Akash Gawas")
def age():
    print("21")
def add():
    print("Vasai,Palghar")
def study():
    print("BE(Bachalor Of Engineering)")

f1=Frame(root,bg="gray",borderwidth=6,relief=SUNKEN)
f1.pack(side=TOP,padx=30,pady=15)
f2=Frame(root,bg="gray",borderwidth=6,relief=SUNKEN)
f2.pack(side=TOP,padx=30,pady=15)
f3=Frame(root,bg="gray",borderwidth=6,relief=SUNKEN)
f3.pack(side=TOP,padx=30,pady=15)
f4=Frame(root,bg="gray",borderwidth=6,relief=SUNKEN)
f4.pack(side=TOP,padx=30,pady=15)


b1=Button(f1,fg="black",text="What is your name?",command=name)
b1.pack()
b2=Button(f2,fg="black",text="what is your age?",command=age)
b2.pack()
b3=Button(f3,fg="black",text="Tell me your address ",command=add)
b3.pack()
b4=Button(f4,fg="black",text="Where you studied?",command=study)
b4.pack()

root.mainloop()