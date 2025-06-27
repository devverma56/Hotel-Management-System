from tkinter import BOTH, BOTTOM, HORIZONTAL, RIDGE, RIGHT, VERTICAL, W, X, Y, Button, Frame, Label, LabelFrame, StringVar, Tk
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class DeatailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Booking system")
        self.root.geometry("1295x590+230+220")
        
        #===============title=============
        lbl_title = Label(self.root, text="ROOM DETAILS", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)
        
        #===============logo=============
        img2 = Image.open(r"C:\Users\91971\Documents\Hotel mangement project\logohotel.png")
        img2 = img2.resize((100, 40))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)
        
        #=================== label frame ===================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", font=("times new roman", 12, "bold"))
        labelframeleft.place(x=5, y=50, width=540, height=350)
        
        
    
        
        # === Floor =================================================
        lbl_floor = Label(labelframeleft, text="Floor", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W, padx=20)
        self.enty_floor = ttk.Entry(labelframeleft, font=("arial", 13, "bold"), width=20)
        self.enty_floor.grid(row=0, column=1, sticky=W)
        
        # === Room No =================================================
        lbl_RoomNo = Label(labelframeleft, text="Room No", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W, padx=20)
        self.enty_RoomNo = ttk.Entry(labelframeleft, font=("arial", 13, "bold"), width=20)
        self.enty_RoomNo.grid(row=1, column=1, sticky=W)
        
        # === Room Type =================================================
        lbl_RoomType = Label(labelframeleft, text="Room Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W, padx=20)
        self.enty_RoomType = ttk.Entry(labelframeleft, font=("arial", 13, "bold"), width=20)
        self.enty_RoomType.grid(row=2, column=1, sticky=W)
        
        #===================== buttons ====================== 
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)
        
        self.btnAdd = Button(btn_frame, text="ADD", font=("arial", 11, "bold"), bg="black", fg="gold", width=10, command=self.add_room)
        self.btnAdd.grid(row=0, column=0, padx=1)
        
        btnUpdate = Button(btn_frame, text="UPDATE", font=("arial", 11, "bold"), bg="black", fg="gold", width=10, command=self.update_room)
        btnUpdate.grid(row=0, column=1, padx=1)
        
        btnDelete = Button(btn_frame, text="DELETE", font=("arial", 11, "bold"), bg="black", fg="gold", width=10, command=self.delete_room)
        btnDelete.grid(row=0, column=2, padx=1)
        
        btnReset = Button(btn_frame, text="RESET", font=("arial", 11, "bold"), bg="black", fg="gold", width=10, command=self.reset_fields)
        btnReset.grid(row=0, column=3, padx=1)
        
        #=================== table frame search system ========================

        Table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", font=("times new roman", 12, "bold"))
        Table_frame.place(x=600, y=55, width=600, height=350)

        # Scrollbars for the table
        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        # Treeview for displaying room details
        self.room_table = ttk.Treeview(Table_frame, columns=("room_id", "floor", "room_no", "room_type"), 
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        # Configuring scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        # Adding headings for the columns
        self.room_table.heading("room_id", text="Room ID")
        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("room_no", text="Room No")
        self.room_table.heading("room_type", text="Room Type")

        # Display the columns as headers
        self.room_table["show"] = "headings"

        # Configuring the column widths
        self.room_table.column("room_id", width=50)
        self.room_table.column("floor", width=100)
        self.room_table.column("room_no", width=100)
        self.room_table.column("room_type", width=150)
        
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        # Fetch rooms into the table
        self.fetch_rooms()

    def connect_db(self):
        return mysql.connector.connect(
            host="localhost", user="root", password="Dev6231@", database="sys"
        )

    def add_room(self):
        floor = self.enty_floor.get()
        room_no = self.enty_RoomNo.get()
        room_type = self.enty_RoomType.get()
        
        if floor == "" or room_no == "" or room_type == "":
            messagebox.showerror("Error", "All fields are required!")
            return
        
        try:
            conn = self.connect_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO rooms (floor, room_no, room_type) VALUES (%s, %s, %s)", 
                           (floor, room_no, room_type))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Room added successfully!")
            self.fetch_rooms()  # Update the table after adding
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"An error occurred: {err}")

    def fetch_rooms(self):
        for row in self.room_table.get_children():
            self.room_table.delete(row)
        
        try:
            conn = self.connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rooms")
            rows = cursor.fetchall()
            for row in rows:
                self.room_table.insert('', 'end', values=row)
            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"An error occurred: {err}")

    def update_room(self):
        selected_item = self.room_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a room to update")
            return
        
        room_id = self.room_table.item(selected_item, 'values')[0]
        floor = self.enty_floor.get()
        room_no = self.enty_RoomNo.get()
        room_type = self.enty_RoomType.get()
        
        if floor == "" or room_no == "" or room_type == "":
            messagebox.showerror("Error", "All fields are required!")
            return
        
        try:
            conn = self.connect_db()
            cursor = conn.cursor()
            cursor.execute("UPDATE rooms SET floor=%s, room_no=%s, room_type=%s WHERE room_id=%s", 
                           (floor, room_no, room_type, room_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Room updated successfully!")
            self.fetch_rooms()  # Update the table after the update
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"An error occurred: {err}")

    def delete_room(self):
        selected_item = self.room_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a room to delete")
            return
        
        room_id = self.room_table.item(selected_item, 'values')[0]
        
        try:
            conn = self.connect_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM rooms WHERE room_id=%s", (room_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Room deleted successfully!")
            self.fetch_rooms()  # Update the table after deletion
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"An error occurred: {err}")

    def reset_fields(self):
        self.enty_floor.delete(0, 'end')
        self.enty_RoomNo.delete(0, 'end')
        self.enty_RoomType.delete(0, 'end')

    def get_cursor(self, event):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content['values']
        
        self.enty_floor.delete(0, 'end')
        self.enty_RoomNo.delete(0, 'end')
        self.enty_RoomType.delete(0, 'end')
        
        self.enty_floor.insert(0, row[1])
        self.enty_RoomNo.insert(0, row[2])
        self.enty_RoomType.insert(0, row[3])

if __name__ == "__main__":
    root = Tk()
    obj = DeatailsRoom(root)
    root.mainloop()
