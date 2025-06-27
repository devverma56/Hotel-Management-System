from tkinter import*
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql
from tkinter import RIDGE, Button, Frame, Label, Tk, Toplevel
from PIL import Image, ImageTk
from customer import Cust_win
from room import Roombooking
from details import DeatailsRoom
from payment import Payment

def main():
    win=Tk()
    aap=Login_window(win)
    win=mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
 
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\91971\Documents\Hotel mangement project\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
        
        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,width=1850,height=1000)
        
        
        frame = Frame(self.root,bg="black")
        frame.place(x=500,y=200,width=400,height=450)
        
        img1 = Image.open(r"C:\Users\91971\Documents\Hotel mangement project\LoginIconAppl.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl_img = Label(frame,image=self.photoimg1,borderwidth=0,bg="black")
        lbl_img.place(x=140,y=10,width=100,height=100)
        
        
        get_str=Label(frame,text="Get started",font=("times new roman",20,"bold"),fg="White",bg="Black")
        get_str.place(x=115,y=120)
        
        
        # label
        lbl_user=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        lbl_user.place(x=90,y=170)
        
        self.txtusr = ttk.Entry(text="username",font=("times new roman",  15,"bold"))
        self.txtusr.place(x=560,y=400,width=250)
        
        password = lbl = Label(frame,text="Passwords",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=90,y=230)
    
        self.txtpsw = ttk.Entry(text="password",font=("times new roman",  15,"bold"),show="*")
        self.txtpsw.place(x=560,y=460,width=250)
        
        
        #======icon image================================
        img2 = Image.open(r"C:\Users\91971\Documents\Hotel mangement project\LoginIconAppl.png")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img = Label(frame,image=self.photoimg2,borderwidth=0,bg="black")
        lbl_img.place(x=60,y=170,width=25,height=25)
        
        img3 = Image.open(r"C:\Users\91971\Documents\Hotel mangement project\lock-512.png")
        img3 = img3.resize((23, 23), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_img = Label(frame,image=self.photoimg3,borderwidth=0,bg="black")
        lbl_img.place(x=60,y=233,width=23,height=23)
        
        loginbtn = Button(frame,text="Login", command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activebackground="red",activeforeground="white")
        loginbtn.place(x=120,y=300,width=150,height=40)
        
        
        registerbtn = Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),bg="black",fg="white",borderwidth=0)
        registerbtn.place(x=10,y=350)
        
        forgetbtn = Button(frame,text="Forget Password",command=self.forget_password_window,font=("times new roman",10,"bold"),bg="black",fg="white",borderwidth=0)
        forgetbtn.place(x=10,y=370)
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)  
             
    def login(self):
        if  self.txtusr.get()=="" or self.txtpsw.get()=="":
            messagebox.showerror("Error", "All fields are required")
            
        elif self.txtusr.get()=="dev" and self.txtpsw.get()=="verma" :
             messagebox.showinfo("Success", "Login successful")
                
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s ",(
                self.txtusr.get(),
                self.txtpsw.get()
            ))
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error", "Invalid username and password")
            else:
                open_main=messagebox.askyesno("Yesno","Acces only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            #====== reset password =============
            
    def reset_pass(self):
        if self.combo_security.get()=="Select":
            
            messagebox.showerror("Error", "Please select security question",parent=self.root2)
        elif self.txt_security_A.get()=="":
            messagebox.showerror("Error", "Please enter security answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error", "Please enter new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtusr.get(),self.combo_security.get(),self.txt_security_A.get(),)
            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Invalid security answer",parent=self.root2)
            else:
                query = ("update register set password=%s where email=%s")
                values=(self.txt_newpass.get(),self.txtusr.get())
                my_cursor.execute(query,values)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Password reset successful, please login new password",parent=self.root2)
                               
    #===================== forget pass window ==============            
    def forget_password_window(self):
        if self.txtusr.get()=="":
            messagebox.showerror("Error", "Please enter username to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            values=(self.txtusr.get(),)
            my_cursor.execute(query,values)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error", "No user found with this email")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("forget password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="blue")
                l.place(x=0,y=10,relwidth=1)
                
                
                security=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
                security.place(x=50,y=80)
                    
                self.combo_security=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state='readonly')
                    
                self.combo_security['values'] = ['Select', 'What is your pet name?', 'What is your favorite color?', 'Where did you first meet your spouse?']
                self.combo_security.current(0)
                self.combo_security.place(x=50,y=110,width=250)
                    
                    
                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                security_A.place(x=50,y=150)
                    
                self.txt_security_A=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security_A.place(x=50,y=180,width=250)
                
                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white")
                new_password.place(x=50,y=220)
                    
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=120,y=290)
        
   
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")
        self.root.geometry("1600x900+0+0")
        
        #==== variables =================================
        
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_email=StringVar()
        self.var_contact=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        
        #==== bg img =================
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\91971\Documents\Hotel mangement project\0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
        bg_lbl = Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
       # ====left image =========
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\91971\Documents\Hotel mangement project\thought-good-morning-messages-LoveSove.jpg")
        left_lbl = Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)
        
        #====frame================================
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        
        lblTitle=Label(frame,text="Registration Form",font=("times new roman",20,"bold"),bg="white",fg="blue")
        lblTitle.place(x=20,y=20)
         
         #===== label=============
        lblName=Label(frame,text=" First Name",font=("times new roman",15,"bold"),bg="white")
        lblName.place(x=50,y=100)
        
        self.txtName=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txtName.place(x=50,y=130,width=250)
        
        
        l_name=Label(frame,text=" Last Name",font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)
        
        contact=Label(frame,text=" Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)
        
        
        email=Label(frame,text=" Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)
        
        
        security=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        security.place(x=50,y=240)
        
        self.combo_security=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state='readonly')
        
        self.combo_security['values'] = ['Select', 'What is your pet name?', 'What is your favorite color?', 'Where did you first meet your spouse?']
        self.combo_security.current(0)
        self.combo_security.place(x=50,y=270,width=250)
        
        
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=370,y=240)
        
        self.txt_security_A=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security_A.place(x=370,y=270,width=250)
        
        
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        password.place(x=50,y=310)
        
        self.txt_password=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"),show="*")
        self.txt_password.place(x=50,y=340,width=250)
        
        
        confirm_password=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirm_password.place(x=370,y=310)
        
        self.txt_confirm_password=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"),show="*")
        self.txt_confirm_password.place(x=370,y=340,width=250)
         
        
        #====== check for buttons================================
        self.var_check= IntVar()
        Checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Term & conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        Checkbtn.place(x=50,y=380)
        
        #====== buttons =================================
        img=Image.open(r"C:\Users\91971\Documents\Hotel mangement project\register-now-button1.jpg")
        img = img.resize((200, 50), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1= Button(frame, image=self.photoimage,command=self.register_data,borderwidth=0, cursor="hand2") 
        b1.place(x=50, y=430, width=200)
        
        img1=Image.open(r"C:\Users\91971\Documents\Hotel mangement project\loginpng.png")
        img1 = img1.resize((200, 50), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2= Button(frame, image=self.photoimage1,borderwidth=0, cursor="hand2") 
        b2.place(x=380, y=430, width=200)
        
        
    def register_data(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_email.get()=="" or self.var_contact.get()=="" or self.var_securityQ.get()=="Select" or self.var_securityA.get()=="" or self.var_pass.get()=="" or self.var_confpass.get()=="":
            messagebox.showerror("Error","All fields are required!")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password should be same!")
        elif not self.var_email.get().endswith("@gmail.com"):
            messagebox.showerror("Error","Please enter a valid Gmail address!")
        elif not self.var_contact.get().isdigit() or len(self.var_contact.get())!=10:    
            messagebox.showerror("Error","Please enter a valid 10-digit contact number!")
            
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree the terms and conditions!")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row!=None:
                messagebox.showerror("Error","Email already exists!")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                    self.var_fname.get(),
                                                    self.var_lname.get(),
                                                    self.var_email.get(),
                                                    self.var_contact.get(),
                                                    self.var_securityQ.get(),
                                                    self.var_securityA.get(),
                                                    self.var_pass.get(),
                ))
            
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registration successful!")     
        

class HotelManagementSystem:
    def __init__(self, root):
        self.root= root
        self.root.title("Hotel Booking system")
        self.root.geometry("1550x800+0+0")
        
        
       #==============Ist img =====================   
        img1 = Image.open(r"C:\Users\91971\Documents\Hotel mangement project\hotel1.png") 
        img1 = img1.resize((1550, 140))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        
        #===================== logo=========================
        img2 = Image.open(r"C:\Users\91971\Documents\Hotel mangement project\logohotel.png") 
        img2 = img2.resize((230, 140))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)
        
        #==================title============================
        lbl_title=Label(self.root,text="Hotel Booking System",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=70)
        
        #================= main frame =====================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=210,width=1550,height=620) 
        
        #==================== menu=========================
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)
        
        #====================== button ==================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=40,width=230,height=190)
        
        cust_btn=Button(btn_frame,text="CUSTOMER",width=22,command=self.cust_details,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)
        
        
        room_btn=Button(btn_frame,text=" ROOM ",width=22,command=self.roombooking,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)
        
        details_btn=Button(btn_frame,text="DETAILS",command=self.DeatailsRoom,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)
        
        
        report_btn=Button(btn_frame,text="PAYMENT",command=self.Payment,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="LOGOUT", command=self.Logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)
        
        
        
        #============== right side image========================
        img3 = Image.open(r"C:\Users\91971\Documents\Hotel mangement project\slide3.jpg") 
        img3 = img3.resize((1310, 590))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)
        
        
        img4 = Image.open(r"C:\Users\91971\Documents\Hotel mangement project\myh.jpg") 
        img4 = img4.resize((230, 210))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lblimg2=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=225,width=230,height=210)
        
        
        img5 = Image.open(r"C:\Users\91971\Documents\Hotel mangement project\khana.jpg") 
        img5 = img5.resize((230, 190))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lblimg3=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg3.place(x=0,y=420,width=230,height=190)
           
        
    def cust_details(self):
        self.new_Window=Toplevel(self.root)
        self.app=Cust_win(self.new_Window)
        
    def roombooking(self):
        self.new_Window=Toplevel(self.root)
        self.app=Roombooking(self.new_Window)
        
    def DeatailsRoom(self):
        self.new_Window=Toplevel(self.root)
        self.app=DeatailsRoom(self.new_Window)
    
    def Payment(self):
        self.new_Window = Toplevel(self.root)
        self.app = Payment(self.new_Window)
        
    def Logout(self):
        self.root.destroy() 
         

if __name__ == "__main__":
    main()
