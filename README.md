# 🎓 Student Fee Management System  

A simple **Python-based console application** to manage student fee records.  
Built using **OOP principles** with `Student` class, JSON database, and separate modules for authentication, database handling, and menus.  

---

##  Features  
-  **Admin**  
  - Add new students with course & fee details  
  - Auto-generate **default password** for new students (`Name@ID`)  
  - View all student records  
  - Secure login with admin password  

-  **Student Panel**  
  - Login with Student ID and password  
  - View fee balance  
  - Make payments  

-  **Persistent Data**  
  - All records stored in `student.json`  
  - Automatically updated after every transaction  

---
##  Project Structure  

Student-Fee-Management-System/
│── main.py # Main entry point
│── auth.py # Handles login system
│── database.py # Load & save JSON data
│── student.py # Student class
│── student.json # Stores student records
│── README.md # Documentation

##  Future Plan For This Mini Project
- ✅ Add default password generator for new students

- ✅ Improve UI with Tkinter desktop app

- ✅ Convert to Flask/Django web app for online use
