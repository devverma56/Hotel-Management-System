import re
from tkinter import BOTH, BOTTOM, END, HORIZONTAL, RIDGE, RIGHT, VERTICAL, W, X, Y, Button, Frame, Label, LabelFrame, StringVar, Tk
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Cust_win:
    def __init__(self, root):
        self.root= root
        self.root.title("Hotel Booking system")
        self.root.geometry("1295x590+230+220")
        
    #==================== variable================
        self.var_ref=StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))
        
        
        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_address=StringVar()

        
        
        #===============title=============#
        
        lbl_title=Label(self.root,text="ADD TO CUSTOMER",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=60)
        
        #===============logo=============
        img2 = Image.open(r"C:\Users\91971\Documents\Hotel mangement project\logohotel.png") 
        img2 = img2.resize((200, 61))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=200,height=61)
        
        #=================== lable frame ===================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Custumer Details",font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=60,width=425,height=490)
        
        #=====================lable ands entry ==============
        #custref
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        enty_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, width=29, font=("arial", 13, "bold"),state="readonly")
        enty_ref.grid(row=0, column=1)
        enty_ref.insert(0," ")

        #cust name
        cname = Label(labelframeleft, text="Customer Name", font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)

        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_cust_name, width=29, font=("arial", 13, "bold"))
        txtcname.grid(row=1, column=1)

       # If you want to set the initial text value, you can use the insert method
        txtcname.insert(0,"")

        #Mother name
        lblmname = Label(labelframeleft, text="Mother Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)

        txtmname = ttk.Entry(labelframeleft, textvariable=self.var_mother, width=29, font=("arial", 13, "bold"))
        txtmname.grid(row=2, column=1)

        # If you want to set the initial text value, you can use the insert method
        txtmname.insert(0, "")

        #gender name combobox
        label_gender=Label(labelframeleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_gender,width=27,state="readonly")
        combo_gender["value"]=("select gender","Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        # postcode
        lblPostCode=Label(labelframeleft,text="PostCode:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        
        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,width=29,font=("arial",13,"bold"))
        txtPostCode.grid(row=4,column=1)
        
        # mobile number
        lblMobile=Label(labelframeleft,text="Mobile Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("arial",13,"bold"))
        txtMobile.grid(row=5,column=1)
        
        #email
        lblEmail=Label(labelframeleft,text="Email ID:",font=("arial",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        
        txtEmail=ttk.Entry(labelframeleft,width=29,textvariable=self.var_email,font=("arial",13,"bold"))
        txtEmail.grid(row=6,column=1)
        
        
        #nationality
        lblNationality=Label(labelframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)
        
        combo_Nationality=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_nationality,width=27,state="readonly")
        combo_Nationality["value"]=("select nationality","Indian","American","Other country")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)
        
        #idproof type combobox
        lblIdProof=Label(labelframeleft,text="ID Proof:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)
        
        combo_id=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_idproof,width=27,state="readonly")
        combo_id["value"]=("select Idproof","AdharCard","PanCard","Passport","drivingLicence")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)
         # ADDRESS
    
        lblAddress=Label(labelframeleft,text=" Address :",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=9,column=0,sticky=W)
        
        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("arial",13,"bold"))
        txtAddress.grid(row=9,column=1)
        
        #ID Number
        lblIdNumber=Label(labelframeleft,text=" ID Number :",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=10,column=0,sticky=W)
        
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_idnumber,width=29,font=("arial",13,"bold"))
        txtIdNumber.grid(row=10,column=1)
        
        #===================== btns ======================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=39)
        
        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpadate=Button(btn_frame,text="Upadate",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpadate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)
        
        #=================== table frame search system========================
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And search System",font=("times new roman",12,"bold"))
        Table_frame.place(x=435,y=60,width=860,height=490)
        
        lblSearch=Label(Table_frame,text=" Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearch.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        
        combo_Search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("select","Mobile","Ref")
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
        details_table.place(x=0,y=50,width=860,height=350)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile",
                                                                   "email","nationality","idproof","address","idnumber")
                                             ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
        
        
        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="Post Code")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="ID Proof")
        self.Cust_Details_Table.heading("address",text="Address")
        self.Cust_Details_Table.heading("idnumber",text="ID Number")
        
        
        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("address",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
    
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()
        
    def validate_mobile(self):
        mobile = self.var_mobile.get()
        if len(mobile) != 10 or not mobile.isdigit():
            return False
        return True

    def validate_email(self):
        email = self.var_email.get()
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if not re.match(regex, email):
            return False
        return True

    def validate_postcode(self):
     postcode = self.var_post.get()
    
    # Check if the postcode is exactly 6 digits long and contains only digits
     if len(postcode) != 6 or not postcode.isdigit():
        messagebox.showwarning("Invalid Postcode", "Postcode must be 6 digits long.", parent=self.root)
        return False
    
     return True


    #==================== Add Customer =================

    def add_data(self):
        if not self.validate_mobile():
            messagebox.showerror("Error", "Invalid Mobile Number. Please enter a valid 10-digit mobile number.", parent=self.root)
            return
        if not self.validate_email():
            messagebox.showerror("Error", "Invalid Email ID. Please enter a valid email address.", parent=self.root)
            return
        if not self.validate_postcode():
            messagebox.showerror("Error", "Invalid Postcode. Please enter a 6-digit postcode.", parent=self.root)
            return
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Dev6231@", database="sys")
            my_cursor = conn.cursor()
            my_cursor.execute("""
                INSERT INTO customer (Ref, Name, Mother, Gender, Postcode, Mobile, Email, Nationality, Idproof, Address, Idnumber)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                self.var_ref.get(),
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_idproof.get(),
                self.var_address.get(),
                self.var_idnumber.get()
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Customer has been added", parent=self.root)
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("","end",values=i)
            conn.commit()
        conn.close()
        
    def get_cuersor(self,event=""):
        cusrsor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cusrsor_row)
        row=content["values"]
        
        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_idproof.set(row[8]),
        self.var_address.set(row[9]),
        self.var_idnumber.set(row[10])
        
        
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s, Mother=%s, Gender=%s, Postcode=%s, Mobile=%s, Email=%s, Nationality=%s, Idproof=%s, Address=%s, Idnumber=%s where Ref=%s",(
                                                                                    self.var_cust_name.get(),
                                                                                    self.var_mother.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_post.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_nationality.get(),
                                                                                    self.var_idproof.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_idnumber.get(),
                                                                                    self.var_ref.get()
                                                                              ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","customer details has been update successfully",parent=self.root)
                      
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    def reset(self):
       # self.var_ref.set("")
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_idproof.set(""),
        self.var_address.set(""),
        self.var_idnumber.set("")
        
        
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))
        
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Dev6231@",database="sys")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM customer WHERE {} LIKE %s".format(self.search_var.get()), ('%' + str(self.txt_search.get()) + '%',))
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("","end",values=i)
            conn.commit()
        conn.close()  
        
         
if __name__ == "__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()
    