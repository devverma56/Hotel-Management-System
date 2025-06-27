from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

import mysql
import mysql.connector


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
        
        
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)
        
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
                
                
                
    
                

    
            
        

         
        
if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
