from datetime import datetime

class Employee:
    def __init__(self, emp_name, date_of_joining, designation, salary):
        self.emp_name = emp_name
        self.date_of_joining = date_of_joining
        self.designation = designation
        self.salary = salary

    def display_employee_info(self):
        print(f"Employee Name: {self.emp_name}")
        print(f"Date of Joining: {self.date_of_joining.strftime('%Y-%m-%d')}")
        print(f"Designation: {self.designation}")
        print(f"Salary: ${self.salary:,.2f}")

def main():
    emp = Employee(
        emp_name="John Doe",
        date_of_joining=datetime(2020, 5, 15),
        designation="Software Engineer",
        salary=75000
    )
    
    emp.display_employee_info()

if __name__ == "__main__":
    main()
