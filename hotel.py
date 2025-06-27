from tkinter import RIDGE, Button, Frame, Label, Tk, Toplevel
from PIL import Image, ImageTk
from customer import Cust_win
from room import Roombooking
from details import DeatailsRoom
from payment import Payment


class HotelManagementSystem:
    def __init__(self, root):
        self.root= root
        self.root.title("Hotel Management system")
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
        lbl_title=Label(self.root,text="Hotel Management System",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
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
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()