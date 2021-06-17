from tkinter import *
root=Tk()
root.geometry("500x250")
root.title("Travel Company")

def Namastey():
    f = open("travelers_info.txt", "a")
    f.write(f"Name: {Namevalue.get()}\n")
    f.write(f"Phone: {Phonevalue.get()}\n")
    f.write(f"Email: {Emailvalue.get()}\n")
    f.write(f"Gender: {Gendervalue.get()}\n")
    f.write(f"payment Mode: {Payment_Modevalue.get()}\n")
    f.write(f"pre-book or not: {FoodServicevalue.get()}\n\n")
    f.close()
    root.destroy()
print("Submitted successfully!")

Label(root,text="Welocome TO Namastey Travels",fg="black",pady=20,font="Helvetica 22 bold underline").grid(row=0,column=3)
Name=Label(root,text="Name").grid(row=1,column=2)
Phone=Label(root,text="Phone").grid(row=2,column=2)
Email=Label(root,text="Email").grid(row=3,column=2)
Gender=Label(root,text="Gender").grid(row=4,column=2)
Payment_Mode=Label(root,text="Payment method").grid(row=5,column=2)

Namevalue=StringVar()
Phonevalue=StringVar()
Emailvalue=StringVar()
Gendervalue=StringVar()
Payment_Modevalue=StringVar()
FoodServicevalue=IntVar()

Nameentry=Entry(root,textvariable=Namevalue).grid(row=1,column=3)
phoneentry=Entry(root,textvariable=Phonevalue).grid(row=2,column=3)
Emailentry=Entry(root,textvariable=Emailvalue).grid(row=3,column=3)
Genderentry=Entry(root,textvariable=Gendervalue).grid(row=4,column=3)
payment_Modeentry=Entry(root,textvariable=Payment_Modevalue).grid(row=5,column=3)

foodservice=Checkbutton(text="want to pre-book your meal?",variable=FoodServicevalue).grid(row=6,column=3)
Button(text="Submit",command=Namastey).grid(row=8,column=3)


root.mainloop()