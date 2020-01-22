from tkinter import *


N_TRIALS = 3
COUNT=-2
N_INTERVALS = 2*N_TRIALS + 1
RELAXING_TIME = 2000
RESTING_TIME = 2000
TASKING_TIME = 2000
start_btn_state = False

def raise_frame(frame):
    frame.tkraise()
    global COUNT
    COUNT+=1
    print(COUNT)

    if (frame == f3 and COUNT==N_INTERVALS):
        frame.after(RESTING_TIME,lambda:raise_frame(f5))

    elif(frame == f5):

        frame.after(RELAXING_TIME,lambda:raise_frame(f6))

    elif frame == f2:
                frame.after(RELAXING_TIME, lambda:raise_frame(f3))
    elif frame == f3:
                frame.after(RESTING_TIME, lambda:raise_frame(f4))

    elif frame == f4:
                 frame.after(TASKING_TIME, lambda:raise_frame(f3))

    elif frame==f6:
        root.destroy()


def finish():
    root.destroy()

def start():
    start_btn_state=True
    raise_frame(f2)


root = Tk()

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)
f6 = Frame(root)



for frame in (f1, f2, f3, f4, f5,f6):
   frame.grid(row = 0, column = 0, sticky='nsew')




lb0=Label(f1, text="blablabla",font=("Arial Bold",10))
lb0.pack(padx = 10, pady=10)
lb1=Label(f1, text="blablabla",font = ("Arial Bold",10),fg = "black")
lb1.pack(padx = 10, pady=10)
lb2 = Label(f1, text="blablabla",font = ("Arial Bold",10),fg = "green")
lb2.pack(padx = 10, pady=10)
lb3 = Label(f1, text="blablabla",font = ("Arial Bold",10),fg = "blue")
lb3.pack(padx = 10, pady=10)
lb4 = Label(f1, text="blablabla",font = ("Arial Bold",10),fg = "red")
lb4.pack(padx = 10, pady=10)
# =============================================================================
# Start Button
# =============================================================================
start_value=BooleanVar()
btn_start=Button(f1, text="Start",font = ("Arial Bold",20), command = start)
btn_start.pack(padx=10,pady=30)
###############################################################################
# =============================================================================
# Close Button
# =============================================================================
close_value=BooleanVar()
btn_close=Button(f1, text="CLOSE",font = ("Arial Bold",20), command=finish)
btn_close.pack(padx=10,pady=30)
###############################################################################


# =============================================================================
# Frame 2
# =============================================================================
Label(f2, text='ACTION 1').pack()
#Button(f2, text='Go to frame 3', command=lambda:raise_frame(f1)).pack()
f2.config(bg='red')

###############################################################################

# =============================================================================
# Frame 3
# =============================================================================
Label(f3, text='ACTION2').pack(side='left')
f3.config(bg='green')
###############################################################################

# =============================================================================
# Frame 4
# =============================================================================
Label(f4, text='ACTION3').pack()
f4.config(bg='blue')

###############################################################################

# =============================================================================
# Frame 5
# =============================================================================
Label(f5, text='RELAXING FINAL').pack()
f5.config(bg='black')
###############################################################################


raise_frame(f1)
root.mainloop()
