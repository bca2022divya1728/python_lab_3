class company:
    def __init__(self,name,city,mobile_no):
        self.name=name
        self.city=city
        self.mobile_no=mobile_no
    
    def display_company_info(self):
        print(f"company Name: {self.name}")
        print(f"city:{self.city}")
        print(f"mobile_no:{self.mobile_no}")
class Employee(company):
    def __init__(self,name,city,mobile_no,emp_name,designation,salary):
        super().__init__(name,city,mobile_no)
        self.emp_name=emp_name
        self.designation=designation
        self.salary=salary
    def display_employee_info(self):
        self.display_company_info()
        print(f"Employee name:{self.emp_name}")
        print(f"designation:{self.designation}")
        print(f"salary:${self.salary:,.2f}")
if __name__=="__main__":
    employee=Employee(
        name="Tech Innovation Inc.",
        city="san Fracisco",
        mobile_no="123_456_7890",
        emp_name="Alice smith",
        designation="software engineer",
        salary=85000.00
        )
    employee.display_employee_info()
    