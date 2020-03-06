from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter.messagebox as tm
from tkinter import PhotoImage
import sqlite3
from functools import partial
import time;

db=sqlite3.connect("vote_system3.db")


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.welcome = ttk.Label(self, text="Welcome To Election Commission of Pakistan")
        self.welcome.config(foreground='white',background='green',font=('Times new roman',49,'bold'))
        self.welcome.pack(side=TOP)
        

        self.localtime= time.asctime(time.localtime(time.time()))
        self.lbl1= Label(self, font = ('times new roman',10),text = self.localtime,fg= "black",bd=10,bg="light green")
        self.lbl1.pack(padx=3,fill=X)

        self.f1=Frame(self, width=999, height = 700,bg = "light green", relief = SUNKEN)
        self.f1.pack(side=RIGHT)
        self.filename = PhotoImage(file = "C:\\Users\\atikul saikh\\Downloads\\PROJECT FINAL changes\\5new.png")
        self.background_label = Label(self.f1, image=self.filename)
        self.background_label.place(bordermode=OUTSIDE, height=550, width=999)

        self.f2=Frame(self, width=300, height = 700,bg = "WHITE", relief = SUNKEN)
        self.f2.pack(side=LEFT)

        self.T = Text(self.f2,height=3, width=30,fg="green")
        self.T.pack(padx=5)
        self.T.insert(END, "Welcome!\nProvide your logins to access \nmore features....!\n\n\n")

        self.label_1 = Label(self.f2,font = ('times new roman',15), text="Username",bg="green",fg="white")
        self.label_1.pack(fill=X,padx=15)
        self.E1 = Entry(self.f2, bd =5)
        self.E1.pack(fill=X,padx=15)

        self.label_2 = Label(self.f2,font = ('times new roman',15), text="Password" ,bg="green",fg="white")
        self.label_2.pack(fill=X,padx=15)
        self.E2 = Entry(self.f2, bd =5,show="*")
        self.E2.pack(fill=X,padx=15)

        def login():
                        username = self.E1.get()
                        password = self.E2.get()
                        if username == "admin" and password == "admin":
                    
                            self.newWindow=Toplevel(self.master)
                            self.app=Home(self.newWindow)

                        elif username=="" or password=="":
                            tm.showerror("Login error", "Please Enter Username and Password",parent=root)      
                        else:
                            tm.showerror("Login error", "Incorrect username or password",parent=root)

        self.b1=Button(self.f2,font=('times new roman',10),padx=5,pady=5,bd=5,fg="white",text = "login",bg="green",height=1,width=5,command=login)
        self.b1.pack()
        
        self.pack()


class Home(Frame):
        def __init__(self,master):
                super().__init__(master)
        
              
                self.Tops = Frame(self, width=1599, height = 60,bg = "dark green", relief = SUNKEN)
                self.Tops.pack(fill=X,side= TOP)

                
                self.f1 = Frame(self, width=2000, height = 300,bg = "white", relief = SUNKEN)
                self.f1.pack(fill=X)
                self.f2 = Frame(self, width=2000, height = 300,bg = "white", relief = SUNKEN)
                self.f2.pack(side=BOTTOM)

                #C = Canvas(self.f1, bg="light green", width=1800, height = 600)
                self.filename = PhotoImage(file = "C:\\Users\\atikul saikh\\Desktop\\a5.png")
                self.background_label = Label(self.f2, image=self.filename,anchor="n")
                self.background_label.grid(column=0,row=6,sticky="wens")


                self.localtime= time.asctime(time.localtime(time.time()))

                self.lblInfo= Label(self.Tops, font = ('times new roman',35,'bold'),text ="       . . . . .ELECTION COMMISSION OF PAKISTAN. . . . .      ",fg= "dark green",bd=10,anchor = 'center' )
                self.lblInfo.grid(row=0,column=0)
                 
                self.lbl1= Label(self.Tops, font = ('times new roman',10),text = self.localtime,fg= "black",bd=10)
                self.lbl1.grid(row=1,column=0)


                boldStyle = ttk.Style ()
                boldStyle.configure("Bold.TButton", font = ('Calibiri','12','bold'),foreground="dark green",background="dark green")
                

                self.add_voter =ttk.Button(self.f1, style = "Bold.TButton",width=25,text="Add Voter",command=self.add_voter)
                self.add_voter.grid(row=1,column=1,padx=100,pady=20)

                self.view_candidate =ttk.Button(self.f1, style = "Bold.TButton",width=25,text="View Candidate",command=self.view_candidate)
                self.view_candidate.grid(row=5,column=10,padx=30,pady=20)

                self.candidate =ttk.Button(self.f1, style = "Bold.TButton",width=25,text="Add candidate",command=self.add_candidate)
                self.candidate.grid(row=1,column=10,padx=30,pady=20)

                self.view_results =ttk.Button(self.f1, style = "Bold.TButton",width=25,text="View Results",command=self.view_results)
                self.view_results.grid(row=4,column=1,padx=200,pady=20)

                self.view_results1 =ttk.Button(self.f1, style = "Bold.TButton",width=25,text="View Voter",command=self.view_voter)
                self.view_results1.grid(row=5,column=1,padx=200,pady=20)

                self.logout=ttk.Button(self.f1, style = "Bold.TButton",width=25,text="Logout",command=self.master.destroy)
                self.logout.grid(row=4,column=10,padx=200,pady=20)

                self.pack()
            
                #

        def view_voter(self):
                self.newWindow=Toplevel(self.master)
                self.app=view_voters(self.newWindow)
        

        
                 
        def add_candidate(self):
                self.newWindow=Toplevel(self.master)
                self.app=candidate(self.newWindow)
        
        def view_candidate(self):
                self.newWindow=Toplevel(self.master)
                self.app=viewcandidates(self.newWindow)
                    
        def add_voter(self):
                self.newWindow = Toplevel(self.master) #open new toplevel window
                self.app = Add_voter(self.newWindow)
 
        def view_voter(self):
                self.newWindow=Toplevel(self.master)
                self.app = view_voter(self.newWindow)

        def view_results(self):
                self.newWindow = Toplevel(self.master) #open new toplevel window
                self.app = View_results(self.newWindow)

    

class candidate(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.Tops = Frame(self, width=1599, height = 60,bg = "dark green", relief = SUNKEN)
        self.Tops.pack(fill=X,side= TOP)

                
        self.f1 = Frame(self, width=1500, height = 700,bg = "white")
        self.f1.pack(side=LEFT,fill=BOTH)

        self.lblInfo= Label(self.Tops, font = ('times new roman',35,'bold'),text ="       . . . . .ELECTION COMMISSION OF PAKISTAN. . . . .      ",fg= "dark green",bd=10,anchor = 'center' )
        self.lblInfo.grid(row=0,column=0)


        self.localtime= time.asctime(time.localtime(time.time()))
        self.lbl1= Label(self.Tops, font = ('times new roman',10),text = self.localtime,fg= "black",bd=10)
        self.lbl1.grid(row=1,column=0)

        self.name=ttk.Label(self.f1,text="CANDIDATE REGISTRATION",relief=SUNKEN)
        self.name.configure(background="dark green",foreground="white",font=('TIMES NEW ROMAN',25))
        self.name.grid(row=45,column=0,padx=30,pady=20)

        self.name=ttk.Label(self.f1,text="Candidate Name")
        self.name.configure(background="White",foreground="dark green",font=('TIMES NEW ROMAN',20))
        self.name.grid(row=50,column=0)
        
        self.name_entry=ttk.Entry(self.f1)
        self.name_entry.grid(row=53,column=0,padx=10)
        
        
        self.location=ttk.Label(self.f1,text="Location")
        self.location.configure(background="White",foreground="dark green",font=('TIMES NEW ROMAN',20))
        self.location.grid(row=90,column=0)

        self.f2 = Frame(self, width=1500, height = 700,bg = "white")
        self.f2.pack(side=RIGHT)

        self.filename = PhotoImage(file = "C:\\Users\\atikul saikh\\Desktop\\a2.png")
        self.background_label = Label(self.f2, image=self.filename)
        self.background_label.grid(row=0,column=0)

        self.location_entry=StringVar()
        self.combobox=ttk.Combobox(self.f1, textvariable=self.location_entry)
        
        data = []
        cur = db.cursor()
        cur.execute("SELECT * FROM location")
        result=cur.fetchall()
        for row in result:
            data.append(row[1])
        self.combobox['values']=data #giving value to combobox which have been stored in list data
        self.combobox.grid(row=91,column=0,padx=10)

        self.party=ttk.Label(self.f1,text="Select Party")
        self.party.configure(background="White",foreground="dark green",font=('TIMES NEW ROMAN',20))
        self.party.grid(row=100,column=0)

        self.party_entry=StringVar()
        self.combobox1=ttk.Combobox(self.f1, textvariable=self.party_entry)
        self.combobox1.config(values=("PTI","PML-N","PPP","MQM"))
        self.combobox1.grid(row=101,column=0)

        self.photo=ttk.Label(self.f1,text="Upload Photo")
        self.photo.configure(background="White",foreground="dark green",font=('TIMES NEW ROMAN',20))
        self.photo.grid(row=110,column=0)

        self.photo_upload =ttk.Button(self.f1,text="Upload file",command=self.upload)
        self.photo_upload.grid(row=115,column=0)



        #self.submit=ttk.Button(self.f1, text="Submit",command=self.add)
        self.submit=Button(self.f1,font=('times new roman',10),padx=5,pady=5,bd=5,fg="white",text = "SUBMIT",bg="dark green",height=1,width=5,command=self.add)
        self.submit.grid(row=125,column=0,padx=20,pady=20)

        self.pack()


        image=""
    def upload(self):
        filename =filedialog.askopenfilename(initialdir = "E:/Images",title = "choose your file",filetypes = (("GIF files","*.gif"),), parent = self)
        global image
        image=filename
        tm.showinfo("congratulations","You have successfully uploaded picture.",parent=self)

        #self.newWindow=Toplevel(self.master)
        #self.app=preview (self.newWindow)       
        
    def add(self):
        name=self.name_entry.get()
        city=self.location_entry.get()
        party=self.party_entry.get()
        global image
        
        if name=="" or city=="" or party=="" or image=="":
           tm.showerror("Error", "Please Fill required Field",parent=self)
        elif  name.isalpha()==False:
           tm.showerror("Constaint Violation", "Please Enter letters Only in Name",parent=self)
        
        else:
            photo=image
            sql='insert into candidates(name,city,image,party) values(?,?,?,?)' #table elements
            db.execute(sql,(name,city,photo,party)) #value store in table element
            db.commit()
            tm.showinfo("Congratulations!", "You have successfully registered your candidate.",parent=self)
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

        self.filename = PhotoImage(file = "C:\\Users\\atikul saikh\\Desktop\\abc.png")
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

class view_voter(Frame):#extra work
    def __init__(self, master):
        super().__init__(master)

        self.Tops = Frame(self, width=1100, height = 1100,bg = "dark green")
        self.Tops.pack(fill=BOTH)

        self.filename = PhotoImage(file = "C:\\Users\\atikul saikh\\Desktop\\bg.png")
        self.background_label = Label(self.Tops, image=self.filename)
        self.background_label.grid(row=0,column=0)

        self.location=ttk.Label(self.background_label,text="Location",)
        self.location.grid(row=2,column=0,padx=10,pady=10)

        self.location_entry=StringVar() # a variable that will store the entry from the 

        self.combobox=ttk.Combobox(self.background_label, textvariable=self.location_entry) # textvariable shows overhead and its entry will be data in location_entry

        data = []
        cur = db.cursor()
        cur.execute("SELECT * FROM location")
        result=cur.fetchall()
        for row in result:
            data.append(row[1])
        self.combobox['values']=data #giving value to combobox which have been stored in list data

    
        self.combobox.grid(row=2,column=1,padx=5,pady=5)



        
        self.view=ttk.Button(self.background_label, text="View Voters",command=self.view)
        self.view.grid(row=4,columnspan=4,padx=10,pady=10)
        global list2
        list2=[]
        self.pack()

    def view(self):
        global list2
        length=len(list2)
        for x in list2:
                x.destroy()

        self.grid_forget()
        



        data = []
        cur = db.cursor()
        location=self.location_entry.get()
        print(location)
        
        cur.execute("SELECT * FROM registered_voters where city=?",(location,))
        result=cur.fetchall()
        x=10
        for i in result:
                self.name=i[2]
                self.cnic=i[1]
                self.gender=i[4]
                
                

                
                self.name_label=ttk.Label(self.background_label,text=self.name)
                self.name_label.grid(row=x,column=0,padx=10,pady=10)

                
                self.cnic_label=ttk.Label(self.background_label,text=self.cnic)
                self.cnic_label.grid(row=x,column=1,padx=10,pady=10)
                
                self.gender_label=ttk.Label(self.background_label,text=self.gender)
                self.gender_label.grid(row=x,column=2,padx=10,pady=10)

                list2.append(self.name_label)
                list2.append(self.cnic_label)
                
                list2.append(self.gender_label)

    
                x=x+2

                self.pack()




class viewcandidates(Frame):#extra work
    def __init__(self, master):
        super().__init__(master)
        self.Tops = Frame(self, width=1100, height = 1100,bg = "dark green")
        self.Tops.pack(fill=BOTH)

        self.filename = PhotoImage(file = "C:\\Users\\atikul saikh\\Desktop\\bg.png")
        self.background_label = Label(self.Tops, image=self.filename)
        self.background_label.grid(row=0,column=0)


        self.location=ttk.Label(self.background_label,text="Location",)
        self.location.grid(row=2,column=0,padx=10,pady=10)

        self.location_entry=StringVar() # a variable that will store the entry from the 

        self.combobox=ttk.Combobox(self.background_label, textvariable=self.location_entry) # textvariable shows overhead and its entry will be data in location_entry

        data = []
        cur = db.cursor()
        cur.execute("SELECT * FROM location")
        result=cur.fetchall()
        for row in result:
            data.append(row[1])
        self.combobox['values']=data #giving value to combobox which have been stored in list data

    
        self.combobox.grid(row=2,column=1,padx=5,pady=5)



        
        self.view=ttk.Button(self.background_label, text="View Candidates",command=self.view)
        self.view.grid(row=4,columnspan=4,padx=10,pady=10)
        global list2
        list2=[]
        self.pack()
    def view(self):
        global list2
        length=len(list2)
        for x in list2:
                x.destroy()

        self.grid_forget()
        



        data = []
        cur = db.cursor()
        location=self.location_entry.get()
        print(location)
        
        cur.execute("SELECT * FROM candidates where city=?",(location,))
        result=cur.fetchall()
        x=10
        for i in result:
                self.name=i[1]
                self.image=i[3]
                self.city=i[2]
                self.party=i[4]
                
                

                self.photo = PhotoImage(file=self.image)
                self.small_photo=self.photo.subsample(5,5)

                
            
                self.name_label=ttk.Label(self.background_label,text=self.name)
                self.name_label.grid(row=x,column=0,padx=10,pady=10)

                
                self.city_label=ttk.Label(self.background_label,text=self.city)
                self.city_label.grid(row=x,column=1,padx=10,pady=10)
                
                self.party_label=ttk.Label(self.background_label,text=self.party)
                self.party_label.grid(row=x,column=2,padx=10,pady=10)

                

                self.pic=ttk.Label(self.background_label,image=self.small_photo)
                self.pic.image=self.small_photo #prevents image from being cleared
                self.pic.grid(row=x,column=3,padx=10,pady=10)


                list2.append(self.name_label)
                list2.append(self.city_label)
                
                list2.append(self.party_label)
                list2.append(self.pic)

                
                
                
                
               
                x=x+2

    

                

            

                self.pack()
        
#        
      







            

class Add_voter(Frame):
    def __init__(self, master):
            super().__init__(master)
            
            self.Tops = Frame(self, width=1200, height = 100,bg = "dark green", relief = SUNKEN)
            self.Tops.pack(fill=X,side= TOP)

                    
            self.f1 = Frame(self, width=400, height = 700,bg = "white")
            self.f1.pack(fill=Y,side=LEFT)

            self.f2 = Frame(self, width=800, height = 1200,bg = "white")
            self.f2.pack(fill=BOTH)

            self.f3 = Frame(self, width=800, height = 200,bg = "white")
            self.f3.pack(side =BOTTOM,fill=BOTH)

            self.lblInfo= Label(self.Tops, font = ('times new roman',35,'bold'),text ="   . . . .THE ELECTION COMMISSION OF PAKISTAN. . . .       ",fg= "dark green",bd=10,anchor = 'center' )
            self.lblInfo.grid(row=0,column=0)


            self.localtime= time.asctime(time.localtime(time.time()))
            self.lbl1= Label(self.Tops, font = ('times new roman',10),text = self.localtime,fg= "black",bd=10)
            self.lbl1.grid(row=1,column=0)

            self.filename = PhotoImage(file = "C:\\Users\\atikul saikh\\Desktop\\a7.png")
            self.background_label = Label(self.f1, image=self.filename,anchor="center")
            self.background_label.grid(column=0,row=0,sticky="wens",padx=0,pady=90)

            self.filename1 = PhotoImage(file = "C:\\Users\\atikul saikh\\Desktop\\a8.png")
            self.background_label1 = Label(self.f3, image=self.filename1,anchor="center")
            self.background_label1.grid(row=0,column=0)

            self.name=ttk.Label(self.f2,text="VOTER'S REGISTRATION",relief=SUNKEN)
            self.name.configure(background="dark green",foreground="white",font=('TIMES NEW ROMAN',25))
            self.name.grid(row=3,column=0,padx=10,pady=20)
            

            self.name=ttk.Label(self.f2,text="Name")
            self.name.configure(background="White",foreground="dark green",font=('TIMES NEW ROMAN',20))
            self.name.grid(row=5,column=0)
            self.name_entry=ttk.Entry(self.f2)
            self.name_entry.grid(row=5,column=1,padx=5,pady=5)

            
            self.age=ttk.Label(self.f2,text="Age")
            self.age.configure(background="White",foreground="dark green",font=('TIMES NEW ROMAN',20))
            self.age.grid(row=10,column=0)
            self.age_entry=ttk.Entry(self.f2)
            self.age_entry.grid(row=10,column=1,padx=5,pady=5)
            
            self.cnic=ttk.Label(self.f2,text="Cnic")
            self.cnic.configure(background="White",foreground="dark green",font=('TIMES NEW ROMAN',20))
            self.cnic.grid(row=15,column=0)
            self.cnic_entry=ttk.Entry(self.f2)
            self.cnic_entry.grid(row=15,column=1,padx=5,pady=5)

            self.gend=ttk.Label(self.f2,text="Gender")
            self.gend.configure(background="White",foreground="dark green",font=('TIMES NEW ROMAN',20))
            self.gend.grid(row=20,column=0) 
            self.gender=StringVar()
            self.combobox1=ttk.Combobox(self.f2, textvariable=self.gender) #selected value stored in self.location variable.
            self.combobox1.config(values=("Male","Female"))
            self.combobox1.grid(row=20,column=1,padx=5,pady=5)

            self.loc=ttk.Label(self.f2,text="Location")
            self.loc.configure(background="White",foreground="dark green",font=('TIMES NEW ROMAN',20))
            self.loc.grid(row=25,column=0)

            
            self.location=StringVar()# the selected value will be stored in it
            self.combobox=ttk.Combobox(self.f2, textvariable=self.location) #selected value stored in self.location variable.
            data=[]
            cur = db.cursor()
            cur.execute("SELECT * FROM location")
            result=cur.fetchall()
            for row in result:
                data.append(row[1])
            self.combobox['values']=data #giving value to combobox which have been stored in list data
            self.combobox.grid(row=25,column=1,padx=5,pady=5)

            boldStyle = ttk.Style ()
            boldStyle.configure("Bold.TButton", font = ('Calibiri','12','bold'),foreground="green")
            boldStyle.configure("Bold.TButton", font = ('Calibiri','12','bold'),foreground="black")

            self.add_voter =ttk.Button(self.f2, style = "Bold.TButton",text="Submit",command=self.add_voter_submit)
            self.add_voter.grid(row=30,columnspan=4, padx=10, pady=10)

            self.pack()

    def add_voter_submit(self):
            name=self.name_entry.get() #get value from entry box and assign it to variable
            age=self.age_entry.get()
            cnic=self.cnic_entry.get()
            gender=self.gender.get()
            location=self.location.get()
            if name=="" or age=="" or cnic=="" or gender=="" or location=="":
                tm.showerror("Error", "Please fill all the fields",parent=self) #1st argument window name
            elif  name.isalpha()==False:
                tm.showerror("Constaint Violation", "Please Enter letters Only in Name",parent=self)
            elif  age.isnumeric()==False:
                tm.showerror("Constaint Violation", "Please Enter Numbers Only in age",parent=self)

            elif int(age)<18:
                tm.showerror("Error", "Voter should be atleast 18 year of age",parent=self)
            else:
                global db #access database using this connection
                cur = db.cursor() #cur= cursor used to fetch data from database
               
                cur.execute("SELECT * FROM registered_voters WHERE cnic=?", (cnic,)) #cur.execute is query that perform a operation on database, selext * select all columns of rows whose cnic is given and return it
                row = cur.fetchone() # store all value of given row
                if row is None: #empty means voter is not registerd
                    #insert data of voter in database registered_voter table
                     con =sqlite3.connect("Cdatabase.db")

                     
                     cur=con.cursor()
                     cur.execute("SELECT * FROM cnic_numbers")

                     result=cur.fetchall()
                     for row in result:    
                        if(cnic==row[1]):
                     
                            sql='insert into registered_voters(cnic,name,city,gender,age) values(?,?,?,?,?)' # name of table element 
                            db.execute(sql,(cnic,name,location,gender,age)) #excecute what is written above, send variable into table elements
                            db.commit() #perform insertion
                            tm.showinfo("Success", "Voter has been successfully registered.",parent=self)
                            self.master.destroy()
                        else:
                            s=True
                        con.close()
                     if(s==True):
                            tm.showerror("Error", "Not verified",parent=self)
                        
                        
                       
                else:
                    tm.showerror("Error", "Your CNIC is already registered",parent=self)
                
            
root = Tk()
root.title('Welcome to Election Commision of Pakistan')
root.geometry("1300x1285+300+300")
LoginFrame(root)
root.mainloop()

