from tkinter import *

root = Tk()
root.geometry("500x250")
root.title("Dance Academy Form")

Label(root, text="Dance Academy Form", font="helvetica 25 bold underline", pady=4,
      padx=25, fg="white", bg="black", relief=SUNKEN).grid(column=1)

name = Label(root, text="Name: ").grid(row=10)
dob = Label(root, text="DOB: ").grid(row=12)
age = Label(root, text="Age: ").grid(row=14)

nameval = StringVar()
dobval = StringVar()
ageval = StringVar()

name_entry = Entry(root, textvariable = nameval).grid(row=10, column=1)
dob_entry = Entry(root, textvariable = dobval).grid(row=12, column=1)
age_entry = Entry(root, textvariable = ageval).grid(row=14, column=1)



def save():
    f = open("form.txt", "a")
    f.write(f"Name: {nameval.get()}\n")
    f.write(f"DOB: {dobval.get()}\n")
    f.write(f"Age: {ageval.get()}\n\n")
    f.close()
    root.destroy()

Button(root, text="Submit", command=save).grid(column=1)

root.mainloop()
