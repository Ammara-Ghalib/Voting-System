from tkinter import *
from tkinter import ttk
import sqlite3

db=sqlite3.connect("Cdatabase.db")


class View(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.welcome = ttk.Label(self, text="Welcome To National Database and Registration Authority\n \t \t      BESE8B")
        self.welcome.config(foreground='BLACK',background='light yellow',font=('Times new roman',37,'bold'))
        self.welcome.pack(side=TOP,fill = X)

        self.f1 = Frame(self,bg = "black")
        self.f1.pack(side=BOTTOM,fill=BOTH)
        self.photo=ttk.Label(self.f1,text="ID \t \t  CNIC \t \t  NAME  \n  ",anchor="center")
        self.photo.configure(background="black",foreground="light yellow",font=('TIMES NEW ROMAN',20))
        self.photo.pack(padx=50,pady=1)
        cur = db.cursor()
        cur.execute("SELECT * FROM cnic_numbers")
        result=cur.fetchall()
        i=0
        for row in result:
            print(row)
            self.photo=ttk.Label(self.f1,text=str(row[0])+" \t \t  "+str(row[1])+" \t \t  "+str(row[2])+"  \n  ",anchor="center")
            self.photo.configure(background="light yellow",foreground="black",font=('TIMES NEW ROMAN',15))
            self.photo.pack(padx=50,pady=1)
            i+=1

        self.pack()




root = Tk()
root.title('Welcome to National Database and Registration Authority, BESE8B')
root.geometry("800x800+300+300")
View(root)
root.mainloop()
