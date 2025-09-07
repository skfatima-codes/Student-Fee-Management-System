
from student import Student
import database
import auth

def admin_menu(data):
    while True:
        print("\n===== Admin Menu =====")
        print("1. Add Student")
        print("2. View Student Records")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            course = input("Enter Course: ")
            total_fee = int(input("Enter Total Fee: "))
            s = Student(student_id, name, course, total_fee)
            data[student_id] = s.to_dict()
            database.save_data(data)
            print(" Student Added Successfully!")

        elif choice == "2":
            for sid, details in data.items():
                print(f"ID: {sid}, Name: {details['name']}, Balance: {details['balance']}")
        
        elif choice == "3":
            break

def student_menu(data, student_id):
    if student_id not in data:
        print(" Student not found!")
        return

    while True:
        print("\n===== Student Menu =====")
        print("1. View Balance")
        print("2. Make Payment")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            print(f"Balance: {data[student_id]['balance']}")
        elif choice == "2":
            amount = int(input("Enter amount to pay: "))
            data[student_id]['paid_fee'] += amount
            data[student_id]['balance'] -= amount
            database.save_data(data)
            print(" Payment Successful!")
        elif choice == "3":
            break

if __name__ == "__main__":
    data = database.load_data()
    login_role = auth.login()

    if login_role == "admin":
        admin_menu(data)
    elif isinstance(login_role, tuple) and login_role[0] == "student":
        student_menu(data, login_role[1])
