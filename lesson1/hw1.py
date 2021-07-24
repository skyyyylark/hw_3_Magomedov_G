class Employe:
    emp_count = 0
    work_rate = 2
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def display_count(self):
        pass


    def display_employee(self):
        print(f"Name: {self.name}, salary: {self.salary}")


    def change_name(self, new_name):
        print(f" {self.name}'s name has been changed to {new_name}")
        self.name = new_name

    def get_total_salary(self):
        return 