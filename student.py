# student.py
class Student:
    def __init__(self, student_id, name, course, total_fee):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.total_fee = total_fee
        self.paid_fee = 0

    def make_payment(self, amount):
        self.paid_fee += amount

    def get_balance(self):
        return self.total_fee - self.paid_fee

    def to_dict(self):
        return {
            "name": self.name,
            "course": self.course,
            "total_fee": self.total_fee,
            "paid_fee": self.paid_fee,
            "balance": self.get_balance(),
            "password": f"{self.name.lower()}123"  # default password
        }
