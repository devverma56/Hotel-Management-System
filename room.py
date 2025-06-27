from tkinter import BOTH, BOTTOM, HORIZONTAL, RIDGE, RIGHT, VERTICAL, W, Y, Button, Frame, Label, LabelFrame, StringVar, Tk,X
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strptime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Roombooking:
    def __init__(self, root):
        self.root= root
        self.root.title("Hotel Booking system")
        self.root.geometry("1295x590+230+220")
        
        #============variable=============
        
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_subtotal=StringVar()
        self.var_total=StringVar()
        
        
       #===============title=============
        
        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=60)
        
        #===============logo=============
        img2 = Image.open(r"C:\Users\91971\Documents\Hotel mangement project\logohotel.png") 
        img2 = img2.resize((200, 61))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=200,height=61)
        
        #=================== lable frame ===================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roombooking Details",font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=60,width=425,height=490)
      
        #=====================lable ands entry ==============
        #custcontact
        lbl_cust_contact = Label(labelframeleft, text="Customer contact", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        enty_contact = ttk.Entry(labelframeleft,textvariable=self.var_contact, width=20, font=("arial", 13, "bold"))
        enty_contact.grid(row=0, column=1,sticky=W)
        
        #=========== fetch btn================
        
        btnFetchData=Button(labelframeleft,text="Fetch Data",command=self.Fetch_contact,font=("arial",9,"bold"),bg="black",fg="gold",width=10)
        btnFetchData.place(x=330,y=4)
        
        
        #check in data 
        check_in_date = Label(labelframeleft, text="Check in date:", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date = ttk.Entry(labelframeleft,textvariable=self.var_checkin ,width=29, font=("arial", 13, "bold"))
        txtcheck_in_date.grid(row=1, column=1)
        
       #custumer in out date
        
        lbl_check_Out = Label(labelframeleft, text="Check out date:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_check_Out.grid(row=2, column=0, sticky=W)

        txt_check_Out = ttk.Entry(labelframeleft, textvariable=self.var_checkout,width=29, font=("arial", 13, "bold"))
        txt_check_Out.grid(row=2, column=1)
        
        #room type
        
        lbl_RoomType = Label(labelframeleft, text="Room type:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=3, column=0, sticky=W)

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=("Single","Double","Laxary")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)
        #Available room
        
        lblRoomAvilable = Label(labelframeleft, text="Available room:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblRoomAvilable.grid(row=4, column=0, sticky=W)

        txtRoomAvilable = ttk.Entry(labelframeleft,textvariable=self.var_roomavailable, width=29, font=("arial", 13, "bold"))
        txtRoomAvilable.grid(row=4, column=1)
        
        #meal
        lblmeal = Label(labelframeleft, text="Meal:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblmeal.grid(row=5, column=0, sticky=W)

        combo_meal=ttk.Combobox(labelframeleft,textvariable=self.var_meal,font=("arial",12,"bold"),width=27,state="readonly")
        combo_meal["value"]=("Breakfast","Lunch","Dinner")
        combo_meal.current(0)
        combo_meal.grid(row=5,column=1)
        
        #no of days
        lblNoOfDays = Label(labelframeleft, text="No of days:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)

        txtlblNoOfDays = ttk.Entry(labelframeleft,textvariable=self.var_noofdays, width=29, font=("arial", 13, "bold"))
        txtlblNoOfDays.grid(row=6, column=1)
        
        
        #paid tax
        
        lblpaidtax = Label(labelframeleft, text="Paid tax:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblpaidtax.grid(row=7, column=0, sticky=W)

        txtpaidtax = ttk.Entry(labelframeleft, textvariable=self.var_paidtax,width=29, font=("arial", 13, "bold"))
        txtpaidtax.grid(row=7, column=1)
        
        #Sub total
        
        lblSubtotal = Label(labelframeleft, text="Sub total:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblSubtotal.grid(row=8, column=0, sticky=W)

        txtSubtotal = ttk.Entry(labelframeleft, textvariable=self.var_subtotal,width=29, font=("arial", 13, "bold"))
        txtSubtotal.grid(row=8, column=1)
        
        #Total cost
        lblIdNumber = Label(labelframeleft, text="Total cost:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)

        txtIdNumber = ttk.Entry(labelframeleft,textvariable=self.var_total,width=29, font=("arial", 13, "bold"))
        txtIdNumber.grid(row=9, column=1)
        
        #==========bill btn==========
        
        
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)
       
       #===================== btns ====================== 
       
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=39)
        
        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpadate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpadate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)
        
        #================ Right side image ============
        
        
        img3 = Image.open(r"C:\Users\91971\Documents\Hotel mangement project\bed.jpg") 
        img3 = img3.resize((520, 220))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=770,y=60,width=520,height=220)
        
        
          #=================== table frame search system========================

        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And search System",font=("times new roman",12,"bold"))
        Table_frame.place(x=430,y=280,width=860,height=270)
        
        lblSearch=Label(Table_frame,text=" Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearch.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        
        combo_Search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("select","Contact","room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
        self.txt_search=StringVar()
        
        txtSearch=ttk.Entry(Table_frame,textvariable=self.txt_search,font=("times new roman",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(Table_frame,text="Search",command=self.search,font=("arial",9,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnShowAll=Button(Table_frame,text="Show All",command=self.fetch_data,font=("arial",9,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)
        
        
         #======================== show data table ===================
         
         
        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=205)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable",
                                                                   "meal","noofdays")
                                             ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        
        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="No Of Days")
        
        
        self.room_table["show"]="headings"
        
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)
    
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
        
        self.fetch_data()
        
    #=============== ALL DATA Fetch =====================   
    
    
    def Fetch_contact(self):
      if self.var_contact.get()=="":
        messagebox.showerror("Error","Please enter contact number",parent=self.root)
        
      else:
        conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
        my_cursor=conn.cursor()
        query=("select Name from customer where Mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
        
        if row==None:
          messagebox.showerror("Error","This number not found",parent=self.root)
          
        else:
          conn.commit()
          conn.close()
          
          showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
          showDataframe.place(x=430,y=60,width=340,height=220)
          
          lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
          lblName.place(x=0,y=0)
          
          lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
          lbl.place(x=90,y=0)
          
          
          conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
          my_cursor=conn.cursor()
          query=("select Gender from customer where Mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          
          lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
          lblGender.place(x=0,y=20)
          
          lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
          lbl2.place(x=90,y=20)
          
          
          conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
          my_cursor=conn.cursor()
          query=("select Email from customer where Mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          
          lblGender=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
          lblGender.place(x=0,y=41)
          
          lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
          lbl2.place(x=90,y=41)
          
          
          conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
          my_cursor=conn.cursor()
          query=("select Nationality from customer where Mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          
          lblGender=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
          lblGender.place(x=0,y=65)
          
          lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
          lbl2.place(x=90,y=65)
          
          conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
          my_cursor=conn.cursor()
          query=("select Idproof from customer where Mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          
          lblGender=Label(showDataframe,text="Idproof:",font=("arial",12,"bold"))
          lblGender.place(x=0,y=85)
          
          lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
          lbl2.place(x=90,y=85)
          
          conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
          my_cursor=conn.cursor()
          query=("select Mother from customer where Mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          
          lblGender=Label(showDataframe,text="Mother:",font=("arial",12,"bold"))
          lblGender.place(x=0,y=105)
          
          lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
          lbl2.place(x=90,y=105)
          
          conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
          my_cursor=conn.cursor()
          query=("select Ref from customer where Mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          
          lblGender=Label(showDataframe,text="Ref no:",font=("arial",12,"bold"))
          lblGender.place(x=0,y=125)
          
          lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
          lbl2.place(x=90,y=125)
          
          conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
          my_cursor=conn.cursor()
          query=("select Address from customer where Mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          
          lblGender=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
          lblGender.place(x=0,y=145)
          
          lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
          lbl2.place(x=90,y=145)
          
          conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
          my_cursor=conn.cursor()
          query=("select Idnumber from customer where Mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          
          lblGender=Label(showDataframe,text="Id number:",font=("arial",12,"bold"))
          lblGender.place(x=0,y=165)
          
          lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
          lbl2.place(x=90,y=165)
    
    def add_data(self):
        if self.var_contact.get()==""or self.var_checkin.get=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
            
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                              self.var_contact.get(),
                                                              self.var_checkin.get(),
                                                              self.var_checkout.get(),
                                                              self.var_roomtype.get(),
                                                              self.var_roomavailable.get(),
                                                              self.var_meal.get(),
                                                              self.var_noofdays.get()
                                                              
                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","room has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)     
          
    # fetch data
    
    def fetch_data(self):
      conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from room")
      rows=my_cursor.fetchall()
      if len(rows)!=0:
        self.room_table.delete(*self.room_table.get_children())
        for i in rows:
          self.room_table.insert("","end",values=i)
          conn.commit()
      conn.close()
        
            
            
             
            
        
      
      
   #======== get cursor ==============   
   
    def get_cuersor(self,event=""):
        cusrsor_row=self.room_table.focus()
        content=self.room_table.item(cusrsor_row)
        row=content["values"]
        
        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])
    
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s, check_out=%s, roomtype=%s, roomavailable=%s, meal=%s, noofdays=%s where Contact=%s",(
                                                              self.var_checkin.get(),
                                                              self.var_checkout.get(),
                                                              self.var_roomtype.get(),
                                                              self.var_roomavailable.get(),
                                                              self.var_meal.get(),
                                                              self.var_noofdays.get(),
                                                              self.var_contact.get(),
                                                                              ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","room details has been update successfully",parent=self.root)
                       
    
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this room",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()     
          
    
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_subtotal.set(""),
        self.var_paidtax.set(""),
        self.var_total.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_roomavailable.set(""),
        self.var_roomtype.set(""),
        
        
        x = random.randint(1000, 9999)
        self.var_contact.set(str(x))
        
        
        
    def total(self):
        try:
            inDate = self.var_checkin.get()
            outDate = self.var_checkout.get()
            if not inDate or not outDate:
                messagebox.showerror("Error", "Please enter both check-in and check-out dates", parent=self.root)
                return

            inDate = datetime.strptime(inDate, "%d/%m/%Y")
            outDate = datetime.strptime(outDate, "%d/%m/%Y")
            self.var_noofdays.set(abs(outDate - inDate).days)

            if self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Laxary":
                q1 = float(800)
                q2 = float(1000)
                q3 = float(self.var_noofdays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = "RS." + str("%.2f" % ((q5) * 0.9))
                ST = "RS." + str("%.2f" % (q5))
                TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.9)))
                self.var_paidtax.set(Tax)
                self.var_subtotal.set(ST)
                self.var_total.set(TT)
        
            
            elif self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Laxary":
                q1 = float(900)
                q2 = float(1100)
                q3 = float(self.var_noofdays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = "RS." + str("%.2f" % ((q5) * 0.9))
                ST = "RS." + str("%.2f" % (q5))
                TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.9)))
                self.var_paidtax.set(Tax)
                self.var_subtotal.set(ST)
                self.var_total.set(TT)
                
            elif self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Laxary":
                q1 = float(1000)
                q2 = float(1200)
                q3 = float(self.var_noofdays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = "RS." + str("%.2f" % ((q5) * 0.9))
                ST = "RS." + str("%.2f" % (q5))
                TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.9)))
                self.var_paidtax.set(Tax)
                self.var_subtotal.set(ST)
                self.var_total.set(TT)
                
            elif self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Double":
                q1 = float(400)
                q2 = float(800)
                q3 = float(self.var_noofdays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = "RS." + str("%.2f" % ((q5) * 0.9))
                ST = "RS." + str("%.2f" % (q5))
                TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.9)))
                self.var_paidtax.set(Tax)
                self.var_subtotal.set(ST)
                self.var_total.set(TT)
            elif self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Double":
                q1 = float(650)
                q2 = float(850)
                q3 = float(self.var_noofdays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = "RS." + str("%.2f" % ((q5) * 0.9))
                ST = "RS." + str("%.2f" % (q5))
                TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.9)))
                self.var_paidtax.set(Tax)
                self.var_subtotal.set(ST)
                self.var_total.set(TT)
                
            elif self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Double":
                q1 = float(800)
                q2 = float(1000)
                q3 = float(self.var_noofdays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = "RS." + str("%.2f" % ((q5) * 0.9))
                ST = "RS." + str("%.2f" % (q5))
                TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.9)))
                self.var_paidtax.set(Tax)
                self.var_subtotal.set(ST)
                self.var_total.set(TT)
                
            elif self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Single":
                q1 = float(400)
                q2 = float(700)
                q3 = float(self.var_noofdays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = "RS." + str("%.2f" % ((q5) * 0.9))
                ST = "RS." + str("%.2f" % (q5))
                TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.9)))
                self.var_paidtax.set(Tax)
                self.var_subtotal.set(ST)
                self.var_total.set(TT)    
            elif self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Single":
                q1 = float(400)
                q2 = float(750)
                q3 = float(self.var_noofdays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = "RS." + str("%.2f" % ((q5) * 0.9))
                ST = "RS." + str("%.2f" % (q5))
                TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.9)))
                self.var_paidtax.set(Tax)
                self.var_subtotal.set(ST)
                self.var_total.set(TT)
                
            elif self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Single":
                q1 = float(500)
                q2 = float(800)
                q3 = float(self.var_noofdays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = "RS." + str("%.2f" % ((q5) * 0.9))
                ST = "RS." + str("%.2f" % (q5))
                TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.9)))
                self.var_paidtax.set(Tax)
                self.var_subtotal.set(ST)
                self.var_total.set(TT)    
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)
        
    #================ search ============
    
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM room WHERE {} LIKE %s".format(self.search_var.get()), ('%' + str(self.txt_search.get()) + '%',))
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("","end",values=i)
            conn.commit()
        conn.close()
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()