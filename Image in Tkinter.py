from tkinter import *

root=Tk()
root.geometry("444x233")
root.title("My GUI")

# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE
title_label=Label(text='''Rohit Gurunath Sharma is an Indian international cricketer who plays for Mumbai 
\nin domestic cricket and captains Mumbai Indians in the Indian Premier League as a right-handed batsman and 
\nan occasional right-arm off break bowler. He is the vice-captain of the Indian national team in limited-overs 
\nformats.Outside cricket, Sharma is an active supporter of animal welfare campaigns. He is the official Rhino 
\nAmbassador for WWF-India and is a member of People for the Ethical Treatment of Animals (PETA). He has worked 
\nwith PETA in its campaign to raise awareness of the plight of homeless cats and dogs in India.''',bg="yellow",
    fg="Blue",padx=23,pady=23,font=("Helvetica",16,"bold"),borderwidth=5,relief=SUNKEN)
# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)
title_label.pack(side="left",anchor="nw",fill=Y)

root.mainloop()