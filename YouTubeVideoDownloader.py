from tkinter import *
from pytube import YouTube
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import filedialog
import os
import requests
from io import BytesIO,StringIO
import datetime

root = Tk()
root.geometry("600x350+350+210")
root.resizable(False,False)
root.title("Youtube Video Downloader")
root.iconbitmap("Logopit_1624880464039.ico")
root.configure(bg="gray19")

def our_command(what):
    try:
        if what == "about":
            root1 = Toplevel()
            root1.geometry("405x205+400+270")
            root1.title("About")
            root1.configure(bg="Gray19")
            root1.resizable(False, False)
            root1.iconbitmap("Logopit_1624880464039.ico")

            img1 = Image.open("final_icon.png")
            img1 = img1.resize((202, 95), Image.LANCZOS)
            photo1 = ImageTk.PhotoImage(img1)

            about = Label(root1, image=photo1,bg = "gray19")
            about.grid(row=0, column=0)
            about.place(rely=-0.06, relx=-0.06, anchor="nw")

            text = Message(root1, text='The YouTube Video Downloader\nVersion 1.0 2021\nLakshya Chourasia.\nAll right '
                                     'reserved.\n\nThe YouTube Video Downloader is completely owned by Lakshya Chourasia ('
                                     'B.Tech). This application is made using Tkinter GUI of Python(V 3.0) with '
                                     'the help of Pycharm - Community 2020.3.', bg="gray19", fg="gray89",
                         width=370, justify=LEFT, padx=3)
            text.grid(row=1, column=1, ipadx=500)
            text.place(rely=0.34, relx=0.07)

            root1.mainloop()
        elif what == "exit":
            root.quit()
    except:
        pass

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="About", command=lambda: our_command("about"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=lambda: our_command("exit"))


img = Image.open("final_icon.png")
img = img.resize((243, 114), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)



you = Label(root, fg="White", bg="gray19", image=photo)
you.grid(row=0, column=0)
you.place(relx=0.28, rely=-0.04)

def maini():
    try:
        link = Label(root, text = "Enter your link:",fg = "gray89", bg = "Gray19")
        link.grid(row = 1,column= 0)
        link.config(font=("Bahnschrift",10,"bold"))
        link.place(relx = 0.172, rely = 0.3435,anchor="e")

        entry_box = Entry(root, bg = "gray89",fg = "black",width = 66,bd = 0)
        entry_box.grid(row = 1, column= 0, columnspan=4, padx=107, pady=100, ipady=5,ipadx = 1)


        def my_click():
            try:
                link_given = str(entry_box.get())

                your_video = YouTube(link_given)


                click = Message(root, text = str(your_video.title),bg ="gray19", fg = 'white',width = 400,justify = CENTER)
                click.grid(pady = 17,padx = 99)
                click.config(font=("Bahnschrift", 9, "bold"))


                img_url = your_video.thumbnail_url
                response = requests.get(img_url)
                pilImage = Image.open(BytesIO(response.content))
                pic = pilImage.resize((160, 90), Image.LANCZOS)
                img3 = ImageTk.PhotoImage(pic)
                panel = Label(root, image=img3,bd = 1,relief = GROOVE)
                img3.image = img3
                panel.grid()
                panel.place(relx=0.368, rely=0.43)

                def my_download():
                    try:
                        entry_box.destroy()
                        entry_button.destroy()
                        download_button.destroy()
                        link.destroy()
                        duration = datetime.timedelta(seconds=your_video.length)
                        if len(your_video.title) <= 59:
                                click.config(text = str(your_video.title)+"\n\n\nDuration: "+str(duration)+"\n"+str(your_video.author),justify = LEFT,font =("Bahnschrift", 10),borderwidth = 2,relief = GROOVE)
                        else:
                            click.config(text=str(your_video.title) + "\n\nDuration: " + str(duration) + "\n" + str(your_video.author),
                                             justify=LEFT, font=("Bahnschrift", 10), borderwidth=2, relief=GROOVE)
                        click.grid(padx = 4,pady = 0)
                        click.place(width = 400,relx = 0.0225,rely = 0.27,height = 93)
                        panel.place(relx = 0.7013,rely = 0.27)

                        select = ttk.Combobox(root, values = ["Video(.mp4/webdm)","Audio Only(.mp3/m4a)"])
                        select.config(font = ("kenyan coffee", 9, "bold"))
                        select.grid(padx= 100,pady = 0)
                        select.place(rely = 0.67,relx =0.358)
                        select.current(0)

                        file_path = Entry(root,bg= "gray35",fg = "white",relief = GROOVE)
                        file_path.grid(padx = 7,pady = 0,ipady = 4)
                        file_path.place(relx = 0.0225,rely = 0.560,height = 25,width = 400)

                    except:
                        pass

                    def dialog():
                        try:
                            path = filedialog.askdirectory(title = "Open")
                            file_path.delete(0,END)
                            file_path.insert(0,path)
                        except:
                            pass

                    browse_button = Button(root,text = "Browse",command = dialog,width = 19,bg = "gray19",fg = "gray89")
                    browse_button.config(font=("kenyan coffee", 9,"bold"))
                    browse_button.grid(padx = 100,pady = 5)
                    browse_button.place(relx = 0.720,rely = 0.560)

                    def audio_video():
                        try:
                            if select.get()== "Video(.mp4/webdm)":
                                your_video.streams.get_highest_resolution().download(file_path.get())
                                panel.place(relx=0.7013, rely=0.27)
                            else:
                                out_file=your_video.streams.filter(only_audio=True).first().download(filename=your_video.title+"audio",output_path=file_path.get())
                                base,ext = os.path.splitext(out_file)
                                new_file = base + '.mp3'
                                os.rename(out_file,new_file)
                                panel.place(relx=0.7013, rely=0.27)
                        except:
                            pass

                    download_button1 = Button(root, text="DOWNLOAD", bg="red3", fg="gray89", command=audio_video, width=11, bd=1)
                    download_button1.config(font=("kenyan coffee", 9, "bold"))
                    download_button1.grid()
                    download_button1.place(relx=0.435, rely=0.78)

                    def back():
                        try:
                            file_path.destroy()
                            browse_button.destroy()
                            click.destroy()
                            download_button1.destroy()
                            panel.destroy()
                            select.destroy()
                            back_button.destroy()
                            maini()
                        except:
                            pass

                    back_button = Button(root, text="Back", bd=1, bg="gray89", fg="gray19", width=10, command=back)
                    back_button.config(font=("kenyan coffee", 9, "bold"))
                    back_button.grid()
                    back_button.place(relx=0.442, rely=0.88)

                download_button = Button(root,text = "DOWNLOAD", bg = "red3", fg = "gray89",command = my_download, width = 11,bd = 1)
                download_button.config(font=("kenyan coffee", 9, "bold"))
                download_button.grid()
                download_button.place(relx=0.439, rely=0.86)
            except:
                pass

        entry_button = Button(root,text = "ENTER",bd = 1,bg = "gray89",fg = "gray19",width = 10,command = my_click)
        entry_button.grid(row = 1, column= 0)
        entry_button.config(font=("Bahnschrift", 8, "bold"),height = 0)
        entry_button.place(relx = 0.975, rely = 0.3135,anchor = "ne")

    except:
        pass

maini()
mainloop()
