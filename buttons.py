from tkinter import *

root = Tk()

def my_click():
    myLabel = Label(root, text= "Look I clicked the button")
    myLabel.pack()

myButton = Button(root, text= "Click",padx = 50, pady = 50, command=my_click, fg ="white", bg = "red")
myButton.pack()

root.mainloop()