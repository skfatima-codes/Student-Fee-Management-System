
import database

def login():
    print("===== Login System =====")
    role = input("Enter role (admin/student): ").strip().lower()
    data = database.load_data()

    if role == "admin":
        password = input("Enter admin password: ")
        if password == "adminknowswell123":
            print(" Admin login successful!")
            return "admin"
        else:
            print(" Wrong password!")
            return None

    elif role == "student":
        sid = input("Enter your Student ID: ")
        if sid in data:
            password = input("Enter your password: ")
            if password == data[sid].get("password", ""):
                print("Student login successful!")
                return ("student", sid)
            else:
                print(" Invalid password")
                return None
        else:
            print(" Invalid Student ID")
            return None

    else:
        print(" Invalid role")
        return None
