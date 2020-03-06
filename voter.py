from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tm
from tkinter import PhotoImage
import time
import sys
import os

import sqlite3
from functools import partial

db=sqlite3.connect("vote_system3.db")
def time_ends(self, x):
    if(x==1):self.root.destroy()
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)


        self.welcome = ttk.Label(self, text="Welcome To Election Commission of Pakistan")
        self.welcome.config(foreground='white',background='dark blue',font=('Times new roman',49,'bold'))
        self.welcome.pack(side=TOP)
        
        self.localtime= time.asctime(time.localtime(time.time()))
        self.lbl1= Label(self, font = ('times new roman',10),text = self.localtime,fg= "black",bd=10,bg="light blue")
        self.lbl1.pack(padx=3,fill=X)

        self.f1=Frame(self, width=999, height = 700,bg = "dark blue", relief = SUNKEN)
        self.f1.pack(side=RIGHT,fill=BOTH)
        self.filename = PhotoImage(file = os.getcwd()+"\\v.png")
        self.background_label = Label(self.f1, image=self.filename)
        self.background_label.place(bordermode=OUTSIDE, height=550, width=999)

        self.f2=Frame(self, width=900, height = 700,bg = "light blue", relief = SUNKEN)
        self.f2.pack(side=LEFT,fill = BOTH)

        self.T = Text(self.f2,height=3, width=50,fg="black")
        self.T.pack(padx=5,pady=80)
        self.T.insert(END, "Welcome!\nPlease enter your CNIC number to proceed.\n\n\n")
        
        self.label_1 = Label(self.f2,font = ('times new roman',25), text="CNIC",bg="dark blue",fg="light blue")
        self.label_1.pack(padx=20,pady=2,fill=X)

        self.entry_1 = ttk.Entry(self.f2,font = ('times new roman',20))
        self.entry_1.pack(padx=20,pady=2)

        self.submitbtn =Button(self.f2,font = ('times new roman',25), text="Submit",bg="white",fg="dark blue", command = self._submit_btn_clickked)
        self.submitbtn.pack(padx=20,pady=2)


        self.submitbtn1 =Button(self.f2,font = ('times new roman',25), text="View Result",bg="white",fg="dark blue", command = self.view)
        self.submitbtn1.pack(padx=20,pady=2)    
        self.pack()

    def _submit_btn_clickked(self):
        cnic = self.entry_1.get()
        if cnic == "":
            tm.showerror("CNIC error", "Please Enter your CNIC")
        else:
            #check if the voter is registered or not
            global db
            cur = db.cursor() #read data from database
            cur.execute("SELECT * FROM registered_voters WHERE cnic=?", (cnic,))
            row = cur.fetchone()
            if row is None:
                tm.showerror("CNIC error", "Please register your CNIC before proceeding.")
            else:
                cur = db.cursor()
                cur.execute("SELECT * FROM votes_casted WHERE cnic=?", (cnic,))
                row = cur.fetchone()
                if row is None: #voter has not casted vote before so show him new window to cast vote
                    self.newWindow = Toplevel(self.master)
                    self.app = Cast_vote(self.newWindow,cnic)
                else: #voter has already casted the vote that's why his row exist in votes_casted table
                    tm.showerror("CNIC error", "You have already casted your vote. Please wait for next elections now :)")

    def view(self):
                self.newWindow=Toplevel(self.master)
                self.app=View_results(self.newWindow)

class Cast_vote(Frame):
    
    def __init__(self, master,cnic):
        super().__init__(master)

        ecp=PhotoImage(file=os.getcwd()+'\\ECP-logo.gif')
        self.logo = ttk.Label(self,image=ecp)
        self.logo.image=ecp

        flag=PhotoImage(file=os.getcwd()+'\\PakistanFlag.gif')
        self.flag = ttk.Label(self,image=flag)
        self.flag.image=flag

        self.welcome = ttk.Label(self, text="Welcome To Election Commision of Pakistan")
        self.welcome.config(foreground='green',background='white')
        self.welcome.config(font=('Calibri',15,'bold'))
        #self.welcome.config(wraplength=150)
        self.welcome.config(justify=CENTER)

        self.logo.grid(row=0,column=0)
        self.flag.grid(row=0,column=2)
        self.welcome.grid(row=0,column=1,sticky="nsew")

        #Show Candidates to the voter for casting vote
        global db
        cur = db.cursor()
        cur.execute("SELECT * FROM registered_voters WHERE cnic=?", (cnic,))
        row = cur.fetchone()
        name=row[2]
        city=row[3]

        name_str="Welcome "+name+"! Please select your favourite candidate by clicking on respective picture!"
        self.name= ttk.Label(self, text=name_str)
        self.name.config(font=('Calibri',12,'bold'))
        self.name.config(foreground='green')
        self.name.grid(columnspan=4, padx=10, pady=10)

        cur.execute("SELECT * FROM candidates WHERE city=?", (city,))
        rows = cur.fetchall()

        i=3
        j=0

        for row in rows:

            self.candidate_name=row[1]
            self.candidate_image=row[3]
            self.candidate_party=row[4]
            
            self.photo = PhotoImage(file=self.candidate_image)
            small_photo=self.photo.subsample(5,5)

            boldStyle = ttk.Style ()
            boldStyle.configure("Bold.TButton", font = ('Calibiri','12','bold'))

            self.vote_button = ttk.Button(self, style = "Bold.TButton",image=small_photo,compound=LEFT, text=self.candidate_name+" "+self.candidate_party,command=partial(self.cast_vote,cnic,self.candidate_name,city))
            #partial used to pass function its arguments
            self.vote_button.image=small_photo            
            self.vote_button.grid(row=i,column=j, padx=10, pady=10)
            
            j=j+1 
            if(j==2):
               j=0
               i=i+1
        

        self.pack()
          
    def cast_vote(self,cnic,candidate,city):
        print(candidate)
        print(cnic)
        print(city)
        sql='insert into votes_casted(cnic,candidate,city) values(?,?,?)'#field
        db.execute(sql,(cnic,candidate,city)) #values
        db.commit()
        tm.showinfo("Congratulations!", "You have successfully casted your vote.")
        self.master.destroy() 

class View_results(Frame):
    def __init__(self, master):
        super().__init__(master)


        self.Tops = Frame(self, width=1200, height = 100,bg = "dark green", relief = SUNKEN)
        self.Tops.pack(fill=X,side= TOP)

                
        self.f1 = Frame(self, width=400, height = 700,bg = "black")
        self.f1.pack(side=LEFT)

        self.f2 = Frame(self, width=800, height = 700,bg = "white")
        self.f2.pack(fil=BOTH)

        self.lblInfo= Label(self.Tops, font = ('times new roman',35,'bold'),text ="       . . . . .RESULTS OF ELECTIONS 2018. . . . .      ",fg= "dark green",bd=10,anchor = 'center' )
        self.lblInfo.grid(row=0,column=0,padx=80,pady=20)


        self.localtime= time.asctime(time.localtime(time.time()))
        self.lbl1= Label(self.Tops, font = ('times new roman',10),text = self.localtime,fg= "black",bd=10)
        self.lbl1.grid(row=1,column=0)

        self.filename = PhotoImage(file = os.getcwd()+"//abc.png")
        self.background_label = Label(self.f1, image=self.filename,anchor="s")
        self.background_label.grid(column=0,row=0,sticky="wens")


        self.loc=ttk.Label(self.f2,text="Location")
        self.loc.configure(background="White",foreground="dark green",font=('TIMES NEW ROMAN',20))
        self.loc.grid(row=2,column=0)
        self.location=StringVar()
        self.combobox=ttk.Combobox(self.f2,textvariable=self.location)
        # Fetch location from Database  
        data = []
        cur = db.cursor()
        cur.execute("SELECT * FROM location")
        result=cur.fetchall()
        for row in result:
            data.append(row[1])
        self.combobox['values']=data #giving value to combobox which have been stored in list data
        self.combobox.grid(row=3,column=0,padx=5,pady=5)


        boldStyle = ttk.Style ()
        boldStyle.configure("Bold.TButton", font = ('Calibiri','12','bold'),foreground="green")

        self.submit_button =ttk.Button(self.f2, style = "Bold.TButton",text="Submit",command=self.view_result)
        self.submit_button.grid(row=5,columnspan=4, padx=10, pady=10)


        self.pack()


        global list1
        list1=[]
    def view_result(self):

            global list1
            location=self.location.get()

            for i in range(0, len(list1)):
                list1[i].destroy()

            if location=="":
                tm.showerror("Error", "Please select the location.",parent=self)
            else:

                self.f2.grid_forget()
                self.loc1=ttk.Label(self.f2,text="Candidate")
                self.loc1.configure(background="White",foreground="dark green",font=('TIMES NEW ROMAN',20))
                self.loc1.grid(row=6,column=0,padx=2,pady=10)
                
                
                self.loc2=ttk.Label(self.f2,text="Number of Votes")
                self.loc2.configure(background="White",foreground="dark green",font=('TIMES NEW ROMAN',20))
                self.loc2.grid(row=6,column=1,pady=10)

                 #get name from location
                cur = db.cursor()
                cur.execute("SELECT * FROM candidates WHERE city=?", (location,)) 
                rows = cur.fetchall() #store all rows having same location
                j=7 # show after row
                for row in rows:
                    name=row[1]                
                    cur = db.cursor()
                    cur.execute("SELECT * FROM votes_casted WHERE candidate=?", (name,))
                    result=cur.fetchall()
                    
                    self.name1=ttk.Label(self.f2,text=name)
                    self.name1.grid(row=j,column=0)
                    list1.append(self.name1)
                    
                    self.vote=ttk.Label(self.f2,text=str(len(result)))
                    self.vote.grid(row=j,column=1)
                    list1.append(self.vote)
                        
                   
                    j+=1 #take to next row




root = Tk()
root.title('Welcome to Election Commision of Pakistan')
root.geometry("1300x1285+300+300")
LoginFrame(root)
root.mainloop()
