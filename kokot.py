from tkinter import *
def quit():
    global root
    root.quit()

def _Menu_(frame):
    root = Tk()

    menu = Menu(root)
    root.config(menu=menu)

    label_1 = Label(root, text="Počítadlo", bg="#33C4FF", fg="black", font="courier 60 underline")
    label_1.place(x=60, y=30)

    butt1 = Button(root, command=obvody())
    butt1 = Button(root, text='SecondC', command=root.quit)
    butt1.place(x=100, y=150)
    butt1.config(width=50, height=5)

    root.geometry("1280x720+300+150")
    root.configure(bg="#33C4FF")
    root.iconbitmap(r'math.ico')
    root.title ("Počítadlo")
    root.mainloop()

def obvody(frame):
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

    root.geometry("640x360+300+150")
    root.configure(bg="#00B5FF")
    menu = Menu(root)
    root.iconbitmap(r'math.ico')
    root.title ("Obvody")
    root.mainloop()

_Menu_(frame)
