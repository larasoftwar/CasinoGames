from tkinter import *


def _Menu_():
    root = Tk()

    menu = Menu(root)
    root.config(menu=menu)

    pocMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Kalkulačka", menu=pocMenu)
    pocMenu.add_separator()
    pocMenu.add_command(label="Otevřít", command=kalkulacka)
    pocMenu.add_separator()

    obvMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Obvody", menu=obvMenu)
    obvMenu.add_separator()
    obvMenu.add_command(label="Trojúhelník")
    obvMenu.add_command(label="Čtverec")
    obvMenu.add_command(label="Obdélník")
    obvMenu.add_command(label="Kruh")
    obvMenu.add_command(label="Lichoběžník")
    obvMenu.add_separator()

    obsMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Obsahy", menu=obsMenu)
    obsMenu.add_separator()
    obsMenu.add_command(label="Trojúhelník")
    obsMenu.add_command(label="Čtverec")
    obsMenu.add_command(label="Obdélník")
    obsMenu.add_command(label="Kruh")
    obsMenu.add_command(label="Lichoběžník")
    obsMenu.add_separator()

    preMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Převody jednotek", menu=preMenu)
    preMenu.add_separator()
    preMenu.add_command(label="Hmotnosti")
    preMenu.add_command(label="Vzdálenosti")
    preMenu.add_command(label="Času")
    preMenu.add_separator()

    infMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Informace", menu=infMenu)
    infMenu.add_separator()
    infMenu.add_command(label="Otevřít", command=informace)
    infMenu.add_separator()


    label_1 = Label(root, text="Počítadlo", bg="#33C4FF", fg="black", font="courier 60 underline")
    label_1.place(x=60, y=30)

    butt1 = Button(root, text="OBVODY", bg="#A3DAF0",fg="black", command=obvody, relief="solid")
    butt1.place(x=100, y=150)
    butt1.config(width=50, height=5)

    butt2 = Button(root, text="OBSAHY", bg="#A3DAF0",fg="black", command=obsahy, relief="solid")
    butt2.place(x=100, y=250)
    butt2.config(width=50, height=5)

    butt3 = Button(root, text="PŘEVODY JEDNOTEK", bg="#A3DAF0",fg="black", command=prevody, relief="solid")
    butt3.place(x=100, y=350)
    butt3.config(width=50, height=5)

    butt4 = Button(root, text="KALKULAČKA", bg="#A3DAF0",fg="black", command=kalkulacka, relief="solid")
    butt4.place(x=100, y=450)
    butt4.config(width=50, height=5)

    butt5 = Button(root, text="INFORMACE", bg="#A3DAF0",fg="black", command=informace, relief="solid")
    butt5.place(x=100, y=550)
    butt5.config(width=50, height=5)

    photo = PhotoImage(file="math.png")
    labelphoto = Label(root, image=photo, bg="#33C4FF")
    labelphoto.place(x=620, y=133)

    root.geometry("1280x720+300+150")
    root.configure(bg="#33C4FF")
    root.iconbitmap(r'math.ico')
    root.title ("Počítadlo")
    root.mainloop()

def obvody():
    root = Tk()

    label_1 = Label(root, text="Obvody", bg="#00B5FF", fg="black", font="courier 40 underline")
    label_1.pack()

    butt1 = Button(root, text="TROJÚHELNÍK", bg="#A3DAF0",fg="black", relief="solid")
    butt1.place(relx=0.5, rely=0.25, anchor=CENTER)
    butt1.config(width=20, height=2)

    butt2 = Button(root, text="ČTVEREC", bg="#A3DAF0",fg="black", relief="solid")
    butt2.place(relx=0.5, rely=0.39, anchor=CENTER)
    butt2.config(width=20, height=2)

    butt3 = Button(root, text="OBDÉLNÍK", bg="#A3DAF0",fg="black", relief="solid")
    butt3.place(relx=0.5, rely=0.53, anchor=CENTER)
    butt3.config(width=20, height=2)

    butt4 = Button(root, text="KRUH", bg="#A3DAF0",fg="black", relief="solid")
    butt4.place(relx=0.5, rely=0.67, anchor=CENTER)
    butt4.config(width=20, height=2)

    butt5 = Button(root, text="LICHOBĚŽNÍK", bg="#A3DAF0",fg="black", relief="solid")
    butt5.place(relx=0.5, rely=0.81, anchor=CENTER)
    butt5.config(width=20, height=2)

    root.geometry("1280x720+300+150")
    root.configure(bg="#00B5FF")
    menu = Menu(root)
    root.iconbitmap(r'math.ico')
    root.title ("Obvody")
    root.mainloop()

def obsahy():
    root = Tk()

    label_1 = Label(root, text="Obsahy", bg="#00B5FF", fg="black", font="courier 40 underline")
    label_1.pack()

    butt1 = Button(root, text="TROJÚHELNÍK", bg="#A3DAF0",fg="black", relief="solid")
    butt1.place(relx=0.5, rely=0.25, anchor=CENTER)
    butt1.config(width=20, height=2)

    butt2 = Button(root, text="ČTVEREC", bg="#A3DAF0",fg="black", relief="solid")
    butt2.place(relx=0.5, rely=0.39, anchor=CENTER)
    butt2.config(width=20, height=2)

    butt3 = Button(root, text="OBDÉLNÍK", bg="#A3DAF0",fg="black", relief="solid")
    butt3.place(relx=0.5, rely=0.53, anchor=CENTER)
    butt3.config(width=20, height=2)

    butt4 = Button(root, text="KRUH", bg="#A3DAF0",fg="black", relief="solid")
    butt4.place(relx=0.5, rely=0.67, anchor=CENTER)
    butt4.config(width=20, height=2)

    butt5 = Button(root, text="LICHOBĚŽNÍK", bg="#A3DAF0",fg="black", relief="solid")
    butt5.place(relx=0.5, rely=0.81, anchor=CENTER)
    butt5.config(width=20, height=2)

    root.geometry("640x360+300+150")
    root.configure(bg="#00B5FF")
    menu = Menu(root)
    root.iconbitmap(r'math.ico')
    root.title ("Obvody")
    root.mainloop()
def prevody(): #jednotek
    root = Tk()

    label_1 = Label(root, text="Převody jednotek", bg="#00B5FF", fg="black", font="courier 40 underline")
    label_1.pack()

    butt1 = Button(root, text="Hmotnosti", bg="#A3DAF0",fg="black", relief="solid")
    butt1.place(relx=0.5, rely=0.25, anchor=CENTER)
    butt1.config(width=20, height=2)

    butt2 = Button(root, text="Vzdálenosti", bg="#A3DAF0",fg="black", relief="solid")
    butt2.place(relx=0.5, rely=0.39, anchor=CENTER)
    butt2.config(width=20, height=2)

    butt3 = Button(root, text="Času", bg="#A3DAF0",fg="black", relief="solid")
    butt3.place(relx=0.5, rely=0.53, anchor=CENTER)
    butt3.config(width=20, height=2)

    root.geometry("640x360+300+150")
    root.configure(bg="#00B5FF")
    menu = Menu(root)
    root.iconbitmap(r'math.ico')
    root.title ("Obvody")
    root.mainloop()

def kalkulacka():# plus, mínus, děleno, krát
    root = Tk()
    print ("ts3.czechvoice.tk")
    root.geometry("640x360+300+150")
    root.configure(bg="#00B5FF")
    menu = Menu(root)
    root.iconbitmap(r'math.ico')
    root.title ("Kalkulačka")
    root.mainloop()

def informace():
    root = Tk()

    root.geometry("640x360+300+150")
    root.configure(bg="#00B5FF")
    menu = Menu(root)
    root.iconbitmap(r'math.ico')
    root.title ("Informace")
    root.mainloop()

_Menu_()
