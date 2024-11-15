import sqlite3
from tkinter import *
from tkinter import messagebox
#===========================================#
window = Tk()
window.geometry("400x500")
window.resizable(False, False)
window.config(bg = "lightgray")
#===========================================#
file_name = "Products.db"

connection = sqlite3.connect(file_name)
cursor = connection.cursor()

create_table = """
CREATE TABLE IF NOT EXISTS Products(
Product_Name TEXT,
Number_Of_Product INTEGER,
Price_Of_Product INTEGER,
Final_Price INTEGER)
"""

cursor.execute(create_table)

connection.commit()
connection.close()
#===========================================#
def add():
    Name = ENT_Name.get()
    Number = ENT_Number.get()
    Price = ENT_Price.get()
    Final = ENT_PAtEnd.get()

    file_name = "Products.db"

    connection = sqlite3.connect(file_name)
    cursor = connection.cursor()

    records = [Name, Number, Price, Final]

    insert_query = """
    INSERT INTO Products(Product_Name, Number_Of_Product, Price_Of_Product, Final_Price)
    VALUES(?, ?, ?, ?)
    """

    cursor.execute(insert_query, records)

    ENT_Name.delete(0, END)
    ENT_Number.delete(0, END)
    ENT_Price.delete(0, END)
    ENT_PAtEnd.delete(0, END)

    connection.commit()
    messagebox.showinfo("ورود اطلاعات", "اطلاعات با موفقیت ذخیره شد")
    connection.close
#===========================================#
def see():
    file_name = "Products.db"

    connection = sqlite3.connect(file_name)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")

    record = cursor.fetchall()
    records = []

    for i in record:
        records.append(i)
        messagebox.showinfo("اطلاعات", f"{records}")
        records.clear()

    connection.close()
#===========================================#
def exit():
    window.destroy()
#===========================================#
LBL_Name = Label(window, text = "نام کالا", font = ("Arial", 20), bg = "lightgray")
LBL_Name.place(x = 280, y = 30)
#-------------------------------------------#
LBL_Number = Label(window, text = "تعداد کالا", font = ("Arial", 20), bg = "lightgray")
LBL_Number.place(x = 272, y = 115)
#-------------------------------------------#
LBL_Price = Label(window, text = "قیمت کالا", font = ("Arial", 20), bg = "lightgray")
LBL_Price.place(x = 274, y = 200)
#-------------------------------------------#
LBL_PAtEnd = Label(window, text = "قیمت کل", font = ("Arial", 20), bg = "lightgray")
LBL_PAtEnd.place(x = 276, y = 280)
#===========================================#
ENT_Name = Entry(window, relief = "sunken", bd = 5)
ENT_Name.place(width = 220, height = 30, x = 35, y = 31)
#-------------------------------------------#
ENT_Number = Entry(window, relief = "sunken", bd = 5)
ENT_Number.place(width = 220, height = 30, x = 35, y = 116)
#-------------------------------------------#
ENT_Price = Entry(window, relief = "sunken", bd = 5)
ENT_Price.place(width = 220, height = 30, x = 35, y = 201)
#-------------------------------------------#
ENT_PAtEnd = Entry(window, relief = "sunken", bd = 5)
ENT_PAtEnd.place(width = 220, height = 30, x = 35, y = 281)
#===========================================#
BTN_See = Button(window, text = "مشاهده اطلاعات", command = see, font = ("Arial", 15), relief = "raised", bd = 5)
BTN_See.place(width = 120, height = 50, x = 220, y = 360)
#-------------------------------------------#
BTN_Save = Button(window, text = "ذخیره اطلاعات", command = add, font = ("Arial", 15), relief = "raised", bd = 5)
BTN_Save.place(width = 120, height = 50, x = 50, y = 360)
#-------------------------------------------#
BTN_Exit = Button(window, text = "خروج", command = exit, font = ("Arial", 15), relief = "raised", bd = 5)
BTN_Exit.place(width = 120, height = 50, x = 140, y = 430)
#===========================================#
window.mainloop()