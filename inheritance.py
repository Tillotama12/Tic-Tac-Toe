# class Person:#parent
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def display1(self):
#         print("name is",self.name)
#         print("age is",self.age)
#
# class Student(Person):
#
#     def __init__(self,name,age,city,phone_no):
#         super().__init__(name,age)
#         #self.name=name
#         #self.age=age
#         self.city=city
#         self.phone_no=phone_no
#
#     def display2(self):
#         super().display1()
#         #print("name is",self.name)
#         #print("age is",self.age)
#         print("city is",self.city)
#         print("phone_no is",self.phone_no)
#
# s=Student("Ramu",23,"banglore",9876532147)
# s.display2()

#single inheritance
#1 child class-->1 parent class only
# class Demo:
#     def __init__(self):
#         print("demo class constructor")
#
# class Lanuch(Demo):
#     def __init__(self):
#         print("launch class constructor")
#
# l=Launch()

#multi-level inheritance

# class Grandparent:
#     def __init__(self):
#         print("grandparent constructor")
#         super().__init__()
#
# class Parent(Grandparent):
#     def __init(self):
#         print("parent constructor")
#
#
# class Child(Parent):
#     def __init(self):
#         print("child constructor")
#
#
# c=Child()

#hierarchial inheritance

# class Demo:
#     def __init__(self):
#         print("parent class constructor")
#
# class Child1(Demo):
#     def __init__(self):
#         print("child1 constructor")
#
# class Child2(Demo):
#     def __init__(self):
#         print("child2 constructor")
#         super().__init__()

#c=Child1()
#c=Child2()

#multiple inheritance

# class Demo:
#     def __init__(self):
#         print("parent class constructor")
#
# class Demo1:
#     def __init__(self):
#         print("Demo 1 constructor")
#
# class Launch(Demo,Demo1): #(Demo1,Demo) MRO(method resolution order)
#     def __init__(self):
#         print("Launch class constructor")
#         super().__init__()
#
# l=Launch()

#cyclic inheritance ---> is not possible

# class A(B):
#     pass
#
# class B(A):
#     pass

#hybrid inheritance (assignment)

#case-2

class Demo:
    def __init__(self):
        print("parent constructor")

    def display1(self):
        print("parent instance method")

    @classmethod
    def display2(cls):
        print("parent class method")

    @staticmethod
    def display3():
        print("parent static method")

class Launch(Demo):
    def __init(self):
        #print("child constructor")
        # super().__init__()
        # super().display1()
        # super().display2()
        # super().display3()

l=Launch()
l.display1()
l.display2()
l.display3()
