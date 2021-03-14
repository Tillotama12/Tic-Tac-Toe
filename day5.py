
#ACCESSING MEMBERS(VARIABLE AND METHOD) OF ONE CLASS INSIDE ANOTHER CLASS
'''
class Employee:
    def __init__(self,name,age,sal,city): #constructor
        self.name=name
        self.age=age
        self.sal=sal
        self.city=city

    def display(self): #instance
        print(self.name)
        print(self.age)
        print(self.sal)
        print(self.city)

class Manager:
    def updateSalary(emp): #instead of emp we can also use self
        emp.sal=emp.sal+1500
        emp.name="sam"
        emp.display()

e=Employee("raju",20,25000,"Bangolore")
Manager.updateSalary(e)
''''

#HAS-A relationship vs IS-A relationship

#HAS-A relationship



