class Employee:
    company="Wipro"
    def __init__(self):
        self.name="geeta"
        Employee.age=29

    def method1(self):
        Employee.salary=3400

    @classmethod
    def method2(cls):
        Employee.id=3
        cls.phoneno=9779

e=Employee()
Employee.state="karnataka"
