import mysql.connector
from tkinter import RIDGE, Label, Tk, Button, Entry, Frame, Toplevel
import os
import re  # To use regular expressions for validation

class Payment:
    def __init__(self, root): 
        self.root = root
        self.root.title("Hotel Booking System - Payment")
        self.root.geometry("800x650+230+220")
        self.root.config(bg="#f4f4f9")

        # Title Section
        self.title_frame = Frame(self.root, bg="black", bd=4, relief=RIDGE)
        self.title_frame.place(x=0, y=0, width=800, height=60)

        lbl_title = Label(self.title_frame, text="Payment", font=("times new roman", 25, "bold"), bg="black", fg="gold")
        lbl_title.pack(pady=10)

        # Payment Form Section
        self.form_frame = Frame(self.root, bg="#ffffff", bd=4, relief=RIDGE)
        self.form_frame.place(x=50, y=100, width=700, height=500)

        # Cardholder's Name
        lbl_name = Label(self.form_frame, text="Cardholder's Name:", font=("times new roman", 15), bg="#ffffff", anchor="w")
        lbl_name.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        self.name_entry = Entry(self.form_frame, font=("times new roman", 14), bd=5, relief=RIDGE)
        self.name_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        # Amount Due
        lbl_amount = Label(self.form_frame, text="Amount Due:", font=("times new roman", 15), bg="#ffffff", anchor="w")
        lbl_amount.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.amount_entry = Entry(self.form_frame, font=("times new roman", 14), bd=5, relief=RIDGE)
        self.amount_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        # Card Number
        lbl_card = Label(self.form_frame, text="Card Number:", font=("times new roman", 15), bg="#ffffff", anchor="w")
        lbl_card.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.card_entry = Entry(self.form_frame, font=("times new roman", 14), bd=5, relief=RIDGE)
        self.card_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        # Expiry Date
        lbl_expiry = Label(self.form_frame, text="Expiry Date (MM/YY):", font=("times new roman", 15), bg="#ffffff", anchor="w")
        lbl_expiry.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        self.expiry_entry = Entry(self.form_frame, font=("times new roman", 14), bd=5, relief=RIDGE)
        self.expiry_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        # CVV
        lbl_cvv = Label(self.form_frame, text="CVV:", font=("times new roman", 15), bg="#ffffff", anchor="w")
        lbl_cvv.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        self.cvv_entry = Entry(self.form_frame, font=("times new roman", 14), bd=5, relief=RIDGE)
        self.cvv_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        # Mobile Number
        lbl_mobile = Label(self.form_frame, text="Mobile Number:", font=("times new roman", 15), bg="#ffffff", anchor="w")
        lbl_mobile.grid(row=5, column=0, padx=20, pady=10, sticky="w")
        self.mobile_entry = Entry(self.form_frame, font=("times new roman", 14), bd=5, relief=RIDGE)
        self.mobile_entry.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        # Pay Button
        btn_pay = Button(self.root, text="Pay Now", font=("times new roman", 18, "bold"), bg="green", fg="white", bd=5, relief=RIDGE, command=self.process_payment)
        btn_pay.place(x=300, y=570, width=200, height=40)

    def process_payment(self):
        # Getting values from entry fields
        name = self.name_entry.get()
        amount = self.amount_entry.get()
        card_number = self.card_entry.get()
        expiry = self.expiry_entry.get()
        cvv = self.cvv_entry.get()
        mobile = self.mobile_entry.get()

        # Validate fields (basic validation)
        if not all([name, amount, card_number, expiry, cvv, mobile]):
            self.show_message("All fields are required!")
            return

        # Validate Card Number (Must be 16 digits)
        if not re.match(r"^\d{16}$", card_number):
            self.show_message("Card number must be exactly 16 digits.")
            return

        # Validate Mobile Number (Must be 10 digits)
        if not re.match(r"^\d{10}$", mobile):
            self.show_message("Mobile number must be exactly 10 digits.")
            return
        
        # Validate Expiry Date (MM/YY format)
        if not re.match(r"^(0[1-9]|1[0-2])\/\d{2}$", expiry):
            self.show_message("Expiry date must be in MM/YY format.")
            return
        
        # Insert payment into MySQL database
        try:
            # MySQL connection
            conn = mysql.connector.connect(
                host="localhost",        # Change this to your MySQL server host
                user="root",             # Your MySQL username
                password="Dev6231@",     # Your MySQL password
                database="sys"           # Your database name
            )
            cursor = conn.cursor()

            # Insert payment data into database
            cursor.execute("""
                INSERT INTO payments (amount_due, card_number, expiry_date, cvv, mobile_number, cardholder_name, payment_status)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (amount, card_number, expiry, cvv, mobile, name, "Success"))

            # Commit the transaction
            conn.commit()

            # Close connection
            cursor.close()
            conn.close()

            # Show payment receipt in a new window
            self.show_receipt(amount, card_number, expiry, name, mobile)

        except mysql.connector.Error as err:
            self.show_message(f"Error: {err}")

    def show_receipt(self, amount, card_number, expiry, name, mobile):
        # Create a new window for the receipt
        receipt_window = Toplevel(self.root)
        receipt_window.title("Payment Receipt")
        receipt_window.geometry("400x350")

        # Receipt Details
        receipt_label = Label(receipt_window, text="Payment Receipt", font=("times new roman", 18, "bold"))
        receipt_label.pack(pady=20)

        receipt_details = f"""
        Amount Paid: ${amount}
        Cardholder: {name}
        Mobile: {mobile}
        Card Number: **** **** **** {card_number[-4:]}
        Expiry Date: {expiry}
        Payment Status: Success
        """
        lbl_receipt = Label(receipt_window, text=receipt_details, font=("times new roman", 14), justify="left")
        lbl_receipt.pack(pady=10)

        # Print Button
        btn_print = Button(receipt_window, text="Print Receipt", font=("times new roman", 14, "bold"), bg="blue", fg="white", command=self.print_receipt)
        btn_print.pack(pady=10)

        # Close Button
        btn_close = Button(receipt_window, text="Close", font=("times new roman", 14, "bold"), bg="red", fg="white", command=receipt_window.destroy)
        btn_close.pack(pady=20)

    def print_receipt(self):
        # This function would print the receipt content
        try:
            # Saving receipt details into a text file (you can print any way you like)
            receipt_content = """
            Payment Receipt:
            -------------------
            Amount Paid: ${}
            Cardholder: {}
            Mobile: {}
            Card Number: **** **** **** {}
            Expiry Date: {}
            Payment Status: Success
            """.format(self.amount_entry.get(), self.name_entry.get(), self.mobile_entry.get(), self.card_entry.get()[-4:], self.expiry_entry.get())
            
            # Save the content in a file
            with open("payment_receipt.txt", "w") as file:
                file.write(receipt_content)

            # Print the saved text file
            os.system("notepad /p payment_receipt.txt")  # For Windows

        except Exception as e:
            self.show_message(f"Error printing receipt: {e}")

    def show_message(self, message):
        # Show a simple message window
        message_window = Toplevel(self.root)
        message_window.title("Message")
        message_window.geometry("300x150")

        lbl_message = Label(message_window, text=message, font=("times new roman", 14))
        lbl_message.pack(pady=20)

        btn_close = Button(message_window, text="Close", font=("times new roman", 14, "bold"), bg="red", fg="white", command=message_window.destroy)
        btn_close.pack(pady=20)

if __name__ == "__main__":
    root = Tk()
    payment_app = Payment(root)
    root.mainloop()
