from tkinter import *

root = Tk()
inp = Entry(root)
inp.pack()
inp.insert(0, "Enter your name: ", )

def my_click():
    myLabel = Label(root,text=inp.get())
    myLabel.pack()

my_button = Button(root, text = "click", command= my_click)
my_button.pack()

root.mainloop()