from tkinter import *
root = Tk()
class History():

    def make_history(self,text):
        history = Label(root, text=text, justify=RIGHT, bg="white", fg="gray40", bd=0)
        history.grid(row=0, column=0, columnspan=4, padx=00, pady=0)
        history.place(relx=1.0, rely=0.03, anchor='ne')
    def clear(self):
        self.make_history("")

