import sys
from tkinter import *
import time

def tick():
    time_string = time.strftime("%H:%M:%S")
    if(time_string == "16:35:00"):
        print(time_string)
        root.destroy()
    else:
        clock.config(text=time_string)
        clock.after(200,tick)

root = Tk()
clock = Label(root)
clock.pack()
tick()
root.mainloop()
