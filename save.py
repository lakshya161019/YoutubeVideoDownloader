root.configure(bg = "gray19")


img = PhotoImage(file = "123.png")
photo = img.subsample(12,12)

img1 = PhotoImage(file ="12.png")
photo1 = img1.subsample(28,28)

you = Label(root, fg ="White", bg ="gray19",image = photo)
you.grid(row = 0, column = 0)
you.place(relx = 0.533, rely = - 0.08,anchor="n")

tube = Label(root, fg ="White", bg ="gray19",image = photo1)
tube.grid(row = 0, column = 0)
tube.place(relx = 0.433, rely =- 0.011,anchor="n")

video = Label(root,text = "Video Downloader" ,fg ="White", bg ="gray19")
video.grid(row = 0, column = 0)
video.config(font=("Bahnschrift",10,"bold"))
video.place(relx = 0.5, rely = 0.088,anchor="n")

