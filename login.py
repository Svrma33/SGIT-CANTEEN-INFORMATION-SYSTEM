from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk, ImageFilter
from tkinter import messagebox
import mysql.connector
import time
from datetime import datetime
from data import *
from tkcalendar import Calendar, DateEntry
from tkinter.simpledialog import askstring
from random import randint
from functions import *
import pygame


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1230x750+138+28")        
        self.root.overrideredirect(True)

        img1 = Image.open("C:/Users/SIDDHARTH/Desktop/Login/login bg.png")
        img1 = img1.resize((1230,750), Image.LANCZOS)
        img1_blur = img1.filter(ImageFilter.GaussianBlur)
        self.photoimg1 = ImageTk.PhotoImage(img1_blur)

        lbl_bg= Label(self.root, image=self.photoimg1)
        lbl_bg.place(x=0, y=0, width=1230, height=750)

        frame=Frame(self.root,bg="black")
        frame.place(x=450,y=155,width=340,height=450)

        img2=Image.open("C:/Users/SIDDHARTH/Desktop/Login/Login.png")
        img2=img2.resize((70,70),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black")
        lblimg2.place(x=570,y=160,width=100,height=100)

        login_str=Label(frame,text="LOGIN",font=("Dutch801 XBd BT",25,"bold"),fg="white",bg="black")
        login_str.place(x=109,y=95)

        #label
        Email=Label(frame,text="Email",font=("Times New Roman",15,"bold"),fg="white",bg="black")
        Email.place(x=67,y=153)

        self.txtemail=ttk.Entry(frame,font=("Times New Roman",15))
        self.txtemail.place(x=40,y=185,width=270)

        Password=Label(frame,text="Password",font=("Times New Roman",15,"bold"),fg="white",bg="black")
        Password.place(x=67,y=225)

        self.txtpass=ttk.Entry(frame,font=("Times New Roman",15))
        self.txtpass.place(x=40,y=255,width=270)

        #icon images
        img3=Image.open("C:/Users/SIDDHARTH/Desktop/Login/Email.png")
        img3=img3.resize((30,30),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black")
        lblimg3.place(x=485,y=305,width=30,height=30)

        img4=Image.open("C:/Users/SIDDHARTH/Desktop/Login/Password.png")
        img4=img4.resize((35,25),Image.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        lblimg4=Label(image=self.photoimage4,bg="black")
        lblimg4.place(x=485,y=380,width=35,height=25)

        #LoginButton
        loginbtn=Button(frame,text="Login",command=self.login,font=("Times New Roman",14,"bold"),cursor="hand2",bd=3,relief=RIDGE,fg="black",bg="white",activeforeground="black",activebackground="white")
        loginbtn.place(x=110,y=300,width=110,height=35)

        #RegisterButton
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("Times New Roman",11),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=360,width=160)

        #ForgetpassButton
        loginbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("Times New Roman",11),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=2,y=395,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtemail.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required")
        elif self.txtemail.get()=="siddharth" and self.txtpass.get()=="verma":
            messagebox.showinfo("Success","Welcome")
        else:
            conn=mysql.connector.connect(host="127.0.0.1",user="root",password="124421",database="login")
            my_cursor=conn.cursor()
            my_cursor.execute("select *from registernow where email=%s and password=%s",(
                self.txtemail.get(),
                self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Email & Password")
            else:
                open_main=messagebox.askyesno("Access","Access only admin")
                if open_main>0:
                    self.root.destroy()
                else:
                    if not open_main:
                        return

            conn.commit()
            conn.close()

    #====================================reset password====================================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="127.0.0.1",user="root",password="124421",database="login")
            my_cursor=conn.cursor()
            query=("select *from registernow where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtemail.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update registernow set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtemail.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset",parent=self.root2)
                self.root2.destroy()



    #====================================forget password window====================================        
    
    def forgot_password_window(self):
        if self.txtemail.get()=="":
            messagebox.showerror("Error","Please enter Email Address to reset password")
        else:
            conn=mysql.connector.connect(host="127.0.0.1",user="root",password="124421",database="login")
            my_cursor=conn.cursor()
            query=("select *from registernow where email=%s")
            value=(self.txtemail.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("My Error","Please enter the valid email")
            else:                
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+580+190")
                self.root2.resizable(False,False)

                l=Label(self.root2,text="Forget Password",font=("Times New Roman",20,"bold"),fg="Red")
                l.place(x=0,y=10,width=340)

                security_Q=Label(self.root2,text="Select Security Questions",font=("Times new roman",15,"bold"))
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",12),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Nick Name","Your Pet's Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
                
                security_A=Label(self.root2,text="Security Answer",font=("Times new roman",15,"bold"))
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("Times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("Times new roman",15,"bold"))
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("Times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("Times new roman",15,"bold"),cursor="hand2",fg="white",bg="black",activeforeground="white",activebackground="black")
                btn.place(x=132,y=290)


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1230x750+130+18")
        self.root.resizable(False,False)

        # ==================variables====================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()
        

        #====================background image====================
        img1 = Image.open("C:/Users/SIDDHARTH/Desktop/Login/login bg.png")
        img1 = img1.resize((1230,750), Image.LANCZOS)
        img1_blur = img1.filter(ImageFilter.GaussianBlur)
        self.photoimg1 = ImageTk.PhotoImage(img1_blur)

        lbl_bg= Label(self.root, image=self.photoimg1)
        lbl_bg.place(x=0, y=0, width=1230, height=750)

        #====================main frame====================
        frame=Frame(self.root,bg="white")
        frame.place(x=215,y=102,width=800,height=550)

        register_lbl=Label(frame,text="New User Register",font=("Times new roman",20,"bold"),fg="Red",bg="white")
        register_lbl.place(x=285,y=20)

        #====================label and entry====================
        #row-1
        fname=Label(frame,text="First Name",font=("Times new roman",15,"bold"),bg="white")
        fname.place(x=100,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Times new roman",15))
        fname_entry.place(x=100,y=130,width=250)
        
        lname=Label(frame,text="Last Name",font=("Times new roman",15,"bold"),bg="white")
        lname.place(x=450,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("Times new roman",15))
        lname_entry.place(x=450,y=130,width=250)

        #row-2
        contact=Label(frame,text="Contact Number",font=("Times new roman",15,"bold"),bg="white")
        contact.place(x=100,y=170)

        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("Times new roman",12))
        contact_entry.place(x=100,y=200,width=250)
        
        email=Label(frame,text="Email",font=("Times new roman",15,"bold"),bg="white")
        email.place(x=450,y=170)

        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("Times new roman",12))
        email_entry.place(x=450,y=200,width=250)

        #row-3
        security_Q=Label(frame,text="Select Security Questions",font=("Times new roman",15,"bold"),bg="white")
        security_Q.place(x=100,y=250)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",12),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Nick Name","Your Pet's Name")
        self.combo_security_Q.place(x=100,y=280,width=250)
        self.combo_security_Q.current(0)
        
        security_A=Label(frame,text="Security Answer",font=("Times new roman",15,"bold"),bg="white")
        security_A.place(x=450,y=250)

        security_A_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("Times new roman",15))
        security_A_entry.place(x=450,y=280,width=250)

        #row-4
        pswd=Label(frame,text="Password",font=("Times new roman",15,"bold"),bg="white")
        pswd.place(x=100,y=320)

        pswd_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("Times new roman",15))
        pswd_entry.place(x=100,y=350,width=250)
        
        cpswd=Label(frame,text="Confirm Password",font=("Times new roman",15,"bold"),bg="white")
        cpswd.place(x=450,y=320)

        cpswd_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("Times new roman",15))
        cpswd_entry.place(x=450,y=350,width=250)

        # ==================checkbutton====================
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("Times new roman",12),onvalue=1,offvalue=0)
        checkbtn.place(x=100,y=390)

        # ==================button====================
        img=Image.open("C:/Users/SIDDHARTH/Desktop/Login/register now.png")
        img=img.resize((150,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=150,y=440,width=150)

        img0=Image.open("C:/Users/SIDDHARTH/Desktop/Login/login now.png")
        img0=img0.resize((150,50),Image.LANCZOS)
        self.photoimage0=ImageTk.PhotoImage(img0)
        b1=Button(frame,image=self.photoimage0,command=self.return_login,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=480,y=440,width=150)

        # ==================Function declaration====================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms & condition")
        else:
            conn=mysql.connector.connect(host="127.0.0.1",user="root",password="124421",database="login")
            my_cursor=conn.cursor()
            query=("select *from registernow where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User aleady exist,please try another email")
            else:
                my_cursor.execute("insert into registernow values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                    self.var_fname.get(),
                                                                    self.var_lname.get(),
                                                                    self.var_contact.get(),
                                                                    self.var_email.get(),
                                                                    self.var_securityQ.get(),
                                                                    self.var_securityA.get(),
                                                                    self.var_pass.get()
                                                                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

    def return_login(self):
        self.root.destroy()


    # -----------Global variables----------------------------------------------------------------------------------------------------------------------------------------
LARGE_FONT = ("Verdana", 12)  # Font that we use often in our program for displaying
day = 0
time = 0
date = 0
database_choice = ''
userInputCondition = False  # To check if time and date is set by user or using current time and date
HOURS = [i for i in range(24)]
MINUTES = [i for i in range(60)]


# ---------For the multiple frames-----------------------------------------------------------------------------------------------------------------------------------
class window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for page in (StartPage, ViewStallPage, AllStallsPage, IndividualStallPage, InstructionPage):
            frame = page(container, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]


# ---------The first frame that shows up when you first run the program----------------------------------------------------------------------------------------------
class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # self.musicIsPlaying = True

        # Background Image for the StartPage
        self.background_img = ImageTk.PhotoImage(file='assets/background.png')
        self.background = Label(self, image=self.background_img)
        self.background.place(relwidth=1, relheight=1)

        # -------Label to show current time--------
        self.label_time = Label(self, justify='center')
        self.label_time.place(relx=0.373, rely=0.02)
        self.clock()

        # --------Button to view stalls--------
        self.logo_viewstalls = ImageTk.PhotoImage(file="assets/viewstalls.png")
        self.button_viewstalls = Button(self, image=self.logo_viewstalls, relief='flat', borderwidth=0,\
                                        compound="center", highlightthickness=0,\
                                        command=lambda: controller.show_frame(ViewStallPage))
        self.button_viewstalls.place(x=503, y=357)

        # -------Button to get user input for date and time--------
        self.logo_datetime = ImageTk.PhotoImage(file="assets/datetime.png")
        button_setDateAndTime = Button(self, image=self.logo_datetime, relief='flat', borderwidth=0, compound="center",\
                                       highlightthickness=0, command=lambda: self.calender(controller))
        button_setDateAndTime.place(relx=0.394, rely=0.686)

        # --------Button to see how to use--------
        self.logo_howtouse = ImageTk.PhotoImage(file="assets/howtouse.png")
        self.button_howtouse = Button(self, image=self.logo_howtouse, relief='flat', borderwidth=0, compound="center",\
                                      highlightthickness=0, command=lambda: controller.show_frame(InstructionPage))
        self.button_howtouse.place(x=503, y=559)

        # # --------Button pause or play the music--------
        # self.button_playMusic = Button(self, text='Pause Music', relief='flat', fg='white', bg='#00b150',\
        #                                font='Helvetica 12', height=2, width=10, command=self.music)
        # self.button_playMusic.place(relx=0.90, rely=0.01)

    
    # # --------Function to pause or resume playing the background music------------------------
    # def music(self):
    #     self.musicIsPlaying = not self.musicIsPlaying
    #     if self.musicIsPlaying:
    #         self.button_playMusic.configure(text="Pause Music")
    #         pygame.mixer.music.unpause()
    #         self.musicIsPlaying = True
    #     else:
    #         self.button_playMusic.configure(text="Play Music")
    #         pygame.mixer.music.pause()
    #         self.musicIsPlaying = False

    # --------Clock function to display current time---------------------------
    def clock(self):
        self.now = datetime.now()
        self.time_str = self.now.strftime("%d/%m/%Y %H:%M:%S")
        if self.time_str != '':
            self.label_time.config(text=self.time_str, font='helvetica 26', fg='white', bg='#383838')
        self.after(100, self.clock)

    # --------Function to display calendar and time for user's input---------------------------
    def calender(self, controller):
        global database_choice, day, time, date

        # --------Actions to be taken user presses the ok button after input.----------------
        def updateUserSelection(toplevel_calendar, controller, drop_sel, hour, minute):
            global database_choice, day, time, date, userInputCondition

            # ----------Update Global Variables based on user's inputs-------------
            time = (100 * int(hour)) + int(minute)
            date = drop_sel
            day = datetime.strptime(str(drop_sel), '%Y-%m-%d').weekday()

            # ----------Close the calendar window and update userInputCondition to True-------------
            toplevel_calendar.destroy()
            userInputCondition = True

        # -------Create a TopLevel to be used for displaying calendar-------------
        toplevel_calendar = Toplevel(self, bg='black')
        toplevel_calendar.grab_set()

        # -------Create an Actual Calendar from tkcalendar module for the user to set date and time-------------
        calendar = Calendar(toplevel_calendar, font="Arial 14", selectmode='day', locale='en_US',\
                            mindate=datetime.now(), background='black', foreground='white', \
                            selectbackground='green', bordercolor='blue', normalforeground='blue',\
                            weekendforeground='blue', headersbackground='blue', headersforeground='white', \
                            cursor="hand1", year=int(date.strftime('%Y')), month=int(date.strftime('%m')),\
                            day=int(date.strftime('%d')))
        calendar.pack(fill="both", expand=True)

        # -------Create a Canvas inside TopLevel to be used later-------------
        canvas = Canvas(toplevel_calendar)
        canvas.pack(side=BOTTOM)

        # -------Label for hours-------------
        hour_label = Label(canvas, text="Time", font=LARGE_FONT, fg='white', bg='#00a99e')
        hour_label.pack(side=LEFT)

        # -------Populate values 0-23 in a comboBox-------------
        hour = ttk.Combobox(canvas, state='readonly')
        hour['values'] = HOURS
        hour.config(width=5, font=('Helvetica', 12))
        hour.pack(side=LEFT)
        hour.current(time // 100)

        # -------Label for minutes-------------
        minute_label = Label(canvas, text=":", font=LARGE_FONT, fg='white', bg='#00a99e')
        minute_label.pack(side=LEFT)

        # -------Populate values 0-59 in a comboBox-------------
        minute = ttk.Combobox(canvas, state='readonly')
        minute['values'] = MINUTES
        minute.config(width=5, font=('Helvetica', 12))
        minute.pack(side=LEFT)
        minute.current(time % 100)

        # -------Button for user to press after setting the date and time-------------
        user_button = Button(canvas, width=10, height=1, text="OK", font='Helvetica 10', relief='flat', fg='white',\
                             bg='#00b150', \
                             command=lambda: updateUserSelection(toplevel_calendar, controller,\
                                                                 calendar.selection_get(), hour.get(), minute.get()))
        user_button.pack(side='bottom')


# ---------Second frame in-line after start page---------------------------------------------------------------------------------------------------------------------
class ViewStallPage(Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)

        # Background Image for the ViewStallPage
        self.background_img = ImageTk.PhotoImage(file='assets/stallspage.png')
        self.background = Label(self, image=self.background_img)
        self.background.place(relwidth=1, relheight=1)

        # ----------Mcdonalds Button---------------
        self.logo_mcdonalds = ImageTk.PhotoImage(file="assets/mcdonald.png")
        self.button_mcdonlads = Button(self, image=self.logo_mcdonalds, relief='flat', borderwidth=0, compound="center",\
                                       highlightthickness=0,\
                                       command=lambda: self.stallSelection(controller, "Mac Donald"))
        self.button_mcdonlads.place(x=172, y=148)
        # -----------------------------------------
        # ---------------KFC Button----------------
        self.logo_kfc = ImageTk.PhotoImage(file="assets/kfc.png")
        self.button_kfc = Button(self, image=self.logo_kfc, relief='flat', borderwidth=0, compound="center",\
                                 highlightthickness=0, command=lambda: self.stallSelection(controller, "KFC"))
        self.button_kfc.place(x=531, y=148)
        # -----------------------------------------
        # ---------------Malay BBQ Button----------
        self.logo_malaybbq = ImageTk.PhotoImage(file="assets/malaybbq.png")
        self.button_malaybbq = Button(self, image=self.logo_malaybbq, relief='flat', borderwidth=0, compound="center",\
                                      highlightthickness=0,\
                                      command=lambda: self.stallSelection(controller, "Malay Stall"))
        self.button_malaybbq.place(x=888, y=150)
        # -----------------------------------------
        # ---------------Yong Tau Foo Button-------
        self.logo_ytfoo = ImageTk.PhotoImage(file="assets/ytfoo.png")
        self.button_ytfoo = Button(self, image=self.logo_ytfoo, relief='flat', borderwidth=0, compound="center",\
                                   highlightthickness=0,\
                                   command=lambda: self.stallSelection(controller, "Yong Tau Foo Stall"))
        self.button_ytfoo.place(x=174, y=402)
        # -----------------------------------------
        # ---------------Drinks Button-------------
        self.logo_drinks = ImageTk.PhotoImage(file="assets/drinks.png")
        self.button_drinks = Button(self, image=self.logo_drinks, relief='flat', borderwidth=0, compound="center",\
                                    highlightthickness=0,\
                                    command=lambda: self.stallSelection(controller, "Beverages Stall"))
        self.button_drinks.place(x=532, y=400)
        # -----------------------------------------
        # ---------------Home Button---------------
        self.home_button = Button(self, text='Home', relief='flat', fg='white', bg='#00b150', font='Helvetica 12',\
                                  height=2, width=10, command=lambda: controller.show_frame(StartPage))
        self.home_button.place(x=10, y=10)
        # -----------------------------------------
        # ---------------All Stalls Button---------------
        self.home_button = Button(self, text='All Stalls', relief='flat', fg='white', bg='#00b150', font='Helvetica 12',\
                                  height=2, width=10, command=lambda: controller.show_frame(AllStallsPage))
        self.home_button.place(x=130, y=10)
        # -----------------------------------------
        # ---------------Random Stall Button------------- 
        self.randomStall = ImageTk.PhotoImage(file="assets/randomstall.png")
        self.button_drinks = Button(self, image=self.randomStall, relief='flat', borderwidth=0,\
                                    compound="center", highlightthickness=0,\
                                    command=lambda: self.buttonRandomStall(controller))
        self.button_drinks.place(x=888, y=400)
        # -----------------------------------------

    # ----------Function to Display A Random Stall-------------
    def buttonRandomStall(self, controller):
        # ----------Get all the stall's names from a function-------------
        howManyStall = getAllStallNames()

        # ----------Generate a random stall's name and pass it as argument-------------
        stall = howManyStall[randint(0, len(howManyStall) - 1)]
        self.stallSelection(controller, stall)

    # ----------Function to Display A Random Stall-------------
    def stallSelection(self, controller, stall):
        global database_choice, userInputCondition, date, time, day

        # ----------Update database_choice variable based on user's/random stall selection-------------
        database_choice = stall

        # ----------If user didn't set date and time, update them before retrieving the stall's info for more accuracy-------------
        if (not userInputCondition):
            date, time, day = updateTime()

        # ----------Execute the execute() function first before jumping to IndividualStallPage Frame-------------
        page = self.controller.get_page(IndividualStallPage)
        page.execute()
        controller.show_frame(IndividualStallPage)


# ---------Frame that shows all the stall menus available------------------------------------------------------------------------------------------------------------
class AllStallsPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(bg="black")

        # ---------Background Image for the AllStallsPage-------------------------
        background_image = ImageTk.PhotoImage(file='assets/cool1.jpg')
        image_label = Label(self, image=background_image)
        image_label.place(x=0, y=0)
        image_label.image = background_image

        # ---------------Return to ViewStallPage Button---------------
        self.back_button = Button(self, text='View Stalls', relief='flat', fg='white', bg='#00b150', font='Helvetica 12',\
                                  height=2, width=10, command=lambda: controller.show_frame(ViewStallPage))
        self.back_button.place(x=10, y=10)

        # ---------------Create a empty canvas for future usage---------------
        self.canvas = Canvas(self, width=600, height=700, background='black')
        self.canvas.pack(side=LEFT, expand=True)

        # ---------------Scrollbar for the Canvas---------------
        self.yscrollbar = Scrollbar(self)
        self.yscrollbar.pack(side=LEFT, fill=Y)

        # ---------------Populate a empty frame inside the Canvas for future usage---------------
        self.frame = Frame(self.canvas, bg='black')
        self.frame.pack(fill=Y, expand=False)

        # ---------------Configuration of the Scrollbar for the Canvas---------------
        self.canvas.configure(yscrollcommand=self.yscrollbar.set)
        self.canvas.bind('<Configure>', self.on_configure)
        self.yscrollbar.configure(command=self.canvas.yview)

        # ---------------Configuration of the Scrollbar for the Canvas---------------
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

        # ----------Get all the stall's names from a function-------------
        howManyStall = getAllStallNames()

        # ----------Dynamically create the neccessary widgets for each stall each time it loops-------------
        for stall in howManyStall:
            # ----------Title for each stall-------------
            disp_title = Label(self.frame, text="Click Icon to view " + stall, font=LARGE_FONT, fg='white', bg='black')
            disp_title.pack(expand=1)

            # ----------Button for each stall with picture. Upon pressing, it will display IndividualStallPage with the selected stall-------------
            stall_image = ImageTk.PhotoImage(file=outlet[stall][0])
            image_label = Button(self.frame, image=stall_image, justify=LEFT,\
                                 command=lambda z=stall: self.goToPageTwo(controller, z))
            image_label.pack(expand=1)
            image_label.image = stall_image

            # ----------Label for displaying stall's menu-------------
            disp_menu = Label(self.frame, font=LARGE_FONT, fg='white', bg='black', justify=LEFT, highlightcolor='white')
            disp_menu.pack(expand=1)

            # ----------Frame to show -------------
            bottomframe = Label(self.frame, font=LARGE_FONT, fg='white', bg='black')
            bottomframe.config(text="____________________________________________________________\n")
            bottomframe.pack()

            # ----------Label for displaying stall's menu-------------
            menu_string = get_allMenu(stall, day)
            disp_menu.configure(text=menu_string)

    # ---------------Update the dimensions of the canvas when items are added or deleted---------------
    def on_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    # ----------Function that update the user's stall choice and timing if needed before jumping to IndividualStallPage Frame-------------
    def goToPageTwo(self, controller, stall):
        global database_choice, userInputCondition

        # ---------------Update the database_choice global variable from user's selection---------------
        database_choice = stall

        # ----------If user didn't set date and time, update them before retrieving the stall's info for more accuracy-------------
        if (not userInputCondition):
            date, time, day

        # ----------Execute the execute() function first before jumping to IndividualStallPage Frame-------------
        page = controller.get_page(IndividualStallPage)
        page.execute()
        controller.show_frame(IndividualStallPage)


# ---------Frame that shows individual stall menu and info based on user's input or random stall---------------------------------------------------------------------
class IndividualStallPage(Frame):
    def __init__(self, parent, controller):
        global database_choice
        Frame.__init__(self, parent)

        # ---------Background Image for the IndividualStallPage-------------------------
        self.backgroundImageLbl = Label(self)
        self.backgroundImageLbl.place(x=0, y=0, relwidth=1, relheight=1)

        # ---------------Return to ViewStallPage Button---------------
        back_button = Button(self, text='View Stalls', relief='flat', fg='white', bg='#00b150', font='Helvetica 12', height=2,\
                             width=9, command=lambda: controller.show_frame(ViewStallPage))
        back_button.place(x=10, y=10)

        # ---------------Label to show the address of the selected stall in NTU---------------
        self.address = Label(self, font=LARGE_FONT, justify=LEFT, fg='white', bg='black')
        self.address.place(relx=0.1, rely=0.85)

        # ---------------Label to show the menu of the selected stall---------------
        self.menu = Label(self, justify=LEFT, fg='white', bg='black', font=("Helvetica", 20))
        self.menu.place(relx=0.55, rely=0.35)

        # -------Button to get user input for date and time------------------
        self.logo_datetime = ImageTk.PhotoImage(file="assets/datetime.png")
        button_setDateAndTime = Button(self, text='SET DATE & TIME', relief='flat', fg='white', bg='#00b150',\
                                       font='Helvetica 12', height=2, width=18, borderwidth=0, compound="center", \
                                       highlightthickness=0, command=lambda: self.calender(controller))
        button_setDateAndTime.place(relx=0.96, rely=0.87, anchor="ne")

        # -------Button to display the operating hours of the selected stalls------------------
        disp_OP_Hours = Button(self, text="Operating Hours", relief='flat', fg='white', bg='#00b150',\
                               font='Helvetica 12', height=2, width=14, command=self.print_OP_Hours)
        disp_OP_Hours.place(relx=0.2, rely=0.016, anchor="ne")

        # -------Button to display the Estimated Queue Time of the selected stalls------------------
        disp_queue = Button(self, text="Estimated Queue Time", relief='flat', fg='white', bg='#00b150',\
                            font='Helvetica 12', height=2, width=19, command=self.print_queue)
        disp_queue.place(relx=0.352, rely=0.016, anchor="ne")

        # -------Button to reset/update the time, day, date to current values------------------
        self.reset_time = Button(self, text='RESET TIME', relief='flat', fg='white', bg='#00b150', font='Helvetica 12',\
                                 height=2, width=14, borderwidth=0, compound="center", \
                                 highlightthickness=0, command = self.resetTime)
        self.reset_time.place(relx=0.82, rely=0.87, anchor="ne")

        # -------Button to view the reviews of the stall------------------
        self.review_button = Button(self, text='REVIEWS', relief='flat', fg='white', bg='#00b150', font='Helvetica 12',\
                                    height=2, width=13, borderwidth=0, compound="center", \
                                    highlightthickness=0, command=self.stallReviews)
        self.review_button.place(relx=0.71, rely=0.87, anchor="ne")

    # -------Store the review in other own stall's file that user has entered-------------------
    def postReviews(self, database, frameReview, userReview):
        # -------Append the new review to existing reviews of the stall------------------
        with open(database['Review'], 'a+') as file:
            file.write('\n» ' + userReview)

        # -------Destroy the review frame and display it again with updated reviews------------------
        frameReview.destroy()
        self.stallReviews()

    # -------Function that display the reviews of the stall and user can post review too---------------------
    def stallReviews(self):
        global database_choice, day, time

        # -------Create a TopLevel for displaying reviews of a stall-------------
        toplevel_review = Toplevel(self, bg='black')
        toplevel_review.title("Reviews")
        toplevel_review.wm_geometry("400x400")
        toplevel_review.grab_set()

        # ---------------Label to show reviews of the selected stall---------------
        review = Label(toplevel_review, font=LARGE_FONT, fg='white', bg='black', justify='left')
        review.pack()

        # -------Create a Canvas inside the Toplevel-------------
        canvas = Canvas(toplevel_review)
        canvas.pack(side=BOTTOM)

        # -------Button to post the user's new input review of the stall------------------
        postReviewButton = Button(canvas, text="Post", font=LARGE_FONT, fg='white', bg='#00b150',\
                                  command=lambda: self.postReviews(database, toplevel_review, userReviewEntry.get()))
        postReviewButton.pack(side=RIGHT)

        # -------For user to type review in it------------------
        userReviewEntry = Entry(canvas, font=LARGE_FONT, fg='black', bg='white', width=10)
        userReviewEntry.pack(side=RIGHT)
        userReviewEntry.pack(ipadx=12, ipady=8)

        # -------Get the correct reviews of the selected stall for display------------------
        database = choosing_database(database_choice, time, day)
        with open(database['Review'], 'a+') as file:
            file.seek(0)
            review.config(text=file.read())

    # -------Update the time, day, date to current and display the stall's menu and info based on that conditions------------------
    def resetTime(self):
        # -------Global variable userInputCondition is used to check if the timing, day, date is based on datetime.now() or user's input------------------
        global userInputCondition, date, time, day

        # -------Reset userInputCondition variable and update the time, day, date to current and displaying the correct menu accordingly by executing the execute() function--------
        userInputCondition = False
        date, time, day = updateTime()
        self.execute()

    # -------Function for displaying estimated queue time for the stall-------------------
    def print_queue(self):
        global database_choice, day, time

        # -------Keep prompting the user's input until it is valid------------------
        while True:
            # -------Button for user to cancel setting date and time
            try:
                # -------Prompt user for input-----------------
                noOfpax = (askstring('Estimated waiting time', 'How many people are in queue currently?'))

                #-------If user presses x or cancel button-----------------
                if noOfpax is None:
                    break
                #-------Else try to convert user's input into integer-----------------
                else:
                    noOfpax = int(noOfpax)

            except:
                # -------Display warning if invalid input-----------------
                messagebox.showwarning(title='Estimated waiting time', message='Input only accept integer values')
            else:
                #-------If input is integer, else prompt user again-----------------
                if noOfpax or noOfpax == 0:

                    # -------If input is negative integer, show warning and prompt user again-----------------
                    if noOfpax < 0:
                        messagebox.showwarning(title='Estimated waiting time',\
                                               message='Input only accept NATURAL numbers.')

                    # -------Else get the queue time per pax from the stall's database, display the estimated queuing time and break from the loop-----------------
                    
                    elif noOfpax >= 50:
                            messagebox.showwarning(title='Estimated waiting time',\
                                                   message='Maximum input exceeded. Please enter number less than 50.')
                    else:
                        database = choosing_database(database_choice, time, day)
                        messagebox.showinfo(title=database['Title'],\
                                                message='Estimated Waiting time: {} minutes'.format(\
                                                    (database['Queue'] * (noOfpax + 1))))
                        break

    # -------Function to display Operating Hours of a stall--------------------
    def print_OP_Hours(self):
        global database_choice, day, time

        # -------Get the Operating Hours from the selected stall's database and display it-----------------
        database = choosing_database(database_choice, time, day)
        messagebox.showinfo(title='Operating Hours', message=database['Hours'])

    # --------Function to display calendar and time for user's input----------------
    def calender(self, controller):
        global database_choice, day, time, date

        # --------Update day, time, date based on user's input and show the correct stall's menu----------------
        def updateUserSelection(toplevel_calendar, controller, drop_sel, hour, minute):
            global day, time, date, userInputCondition

            # --------Update day, time, date based on user's input----------------
            time = (100 * int(hour)) + int(minute)
            date = drop_sel
            day = datetime.strptime(str(drop_sel), '%Y-%m-%d').weekday()

            # --------Destroy the calendar frame----------------
            toplevel_calendar.destroy()

            # --------Displaying the correct stall's menu based on user's selection and update userInputCondition to True-----------------------------
            userInputCondition = True
            page = controller.get_page(IndividualStallPage)
            page.execute()
            controller.show_frame(IndividualStallPage)

        # -------Create a TopLevel to be used for displaying calendar-------------
        toplevel_calendar = Toplevel(self, bg='black')
        toplevel_calendar.grab_set()
        
        # -------Create a Actual Calendar from tkcalendar module-------------
        calendar = Calendar(toplevel_calendar, font="Arial 14", selectmode='day', locale='en_US',\
                            mindate=datetime.now(), background='black', foreground='white', \
                            selectbackground='green', bordercolor='blue', normalforeground='blue',\
                            weekendforeground='blue', headersbackground='blue', headersforeground='white', \
                            cursor="hand1", year=int(date.strftime('%Y')), month=int(date.strftime('%m')),\
                            day=int(date.strftime('%d')))
        calendar.pack(fill="both", expand=True)

        # -------Create a Canvas inside TopLevel to be used later-------------
        canvas = Canvas(toplevel_calendar)
        canvas.pack(side=BOTTOM)

        # -------Label for hours-------------
        hour_label = Label(canvas, text="Time", font=LARGE_FONT, fg='white', bg='#00a99e')
        hour_label.pack(side=LEFT)

        # -------Populate values 0-23 (24-hours format) in a comboBox-------------
        hour = ttk.Combobox(canvas, state='readonly')
        hour['values'] = HOURS
        hour.config(width=5, font=('Helvetica', 12))
        hour.pack(side=LEFT)
        hour.current(time // 100)

        # -------Label for hours-------------
        minute_label = Label(canvas, text=":", font=LARGE_FONT, fg='white', bg='#00a99e')
        minute_label.pack(side=LEFT)

        # -------Populate values 0-59 (60 seconds) in a comboBox-------------
        minute = ttk.Combobox(canvas, state='readonly')
        minute['values'] = MINUTES
        minute.config(width=5, font=('Helvetica', 12))
        minute.pack(side=LEFT)
        minute.current(time % 100)

        # -------Button for user to press after setting the date and time-------------
        button = Button(canvas, width=10, height=1, text="OK", font='Helvetica 10', relief='flat', fg='white',bg='#00b150', \
                        command=lambda: updateUserSelection(toplevel_calendar, controller, calendar.selection_get(),\
                                                            hour.get(), minute.get()))
        button.pack(side='bottom')

    # -------Run this function first before showing IndividualStallPage to display the correct stall info and menu-------------
    def execute(self):
        global database_choice, day, time

        # ---------------Display the Image Icon of the stall---------------
        bg_image = ImageTk.PhotoImage(file=outlet[database_choice][1])
        self.backgroundImageLbl.configure(image=bg_image, width=1280, height=721)
        self.backgroundImageLbl.image = bg_image

        # ---------------Display the location of the stall in NTU---------------
        database = choosing_database(database_choice, time, day)
        self.address.configure(text=database['Location'])

        # ---------------Display the title and menu of the stall---------------
        menu_string = database['Title'] + '\n'
        menu_string += get_menu_from_database(database, time, day)
        self.menu.configure(text=menu_string)


# -------For displaying instructions on how to use this application--------------------------------------------------------------------------------------------------
class InstructionPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # ---------------Display the image that consists of the instructions---------------
        self.background_img = ImageTk.PhotoImage(file='assets/instructions.png')
        self.background = Label(self, image=self.background_img)
        self.background.place(relwidth=1, relheight=1)

        # ---------------Return to StartPage---------------
        self.home_button = Button(self, text='Home', relief='flat', fg='white', bg='#00b150', font='Helvetica 12',\
                                  height=2, width=10, command=lambda: controller.show_frame(StartPage))
        self.home_button.place(x=10, y=10)

# ---------Things to do when you press x close button of the window--------------------------------------------------------------------------------------------------
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        GUI.destroy()
        # pygame.mixer.music.stop()

# --------Get the cureent time, date and day when this program first starts up
date, time, day = updateTime()

# --------Add music in the background to enhance the user experience-------------------------------------------------------------------------------------------------
# pygame.mixer.init()
# pygame.mixer.music.load("assets/Welcome to SGIT.ogg")
# pygame.mixer.music.play(-1)


if __name__ =="__main__":
    main()

# --------MAIN GUI---------------------------------------------------------------------------------------------------------------------------------------------------
GUI = window()
GUI.title("SGIT Canteen Management System")
GUI.geometry('1275x670+120+50')
GUI.resizable(False, False)
GUI.protocol("WM_DELETE_WINDOW", on_closing)
GUI.mainloop()


