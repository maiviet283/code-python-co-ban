class Person:
    count = 0 # bien cua person
    def __init__(self,name,age):
        self.__name = name # bien instance
        self.__age = age
        Person.increment_count()

    @property #get
    def name(self):
        return self.__name
    
    @property #get
    def age(self):
        return self.__age
    
    @name.setter #set
    def set_name(self,name):
        self.__name = name

    @age.setter #set
    def set_age(self,age):
        self.__age = age

    @classmethod
    def increment_count(cls):
        cls.count += 1

    def greeting(self):
        print("Hello")

    @staticmethod
    def cls_infomation():
        print(f"The infomation of class : ")
        print(f"\t - Class Name : {Person.__name__}")
        print(f"\t - Base Class : {Person.__base__}")
        print(f"\t - The Number ofobject: {Person.count}")
    
    def __str__(self):
        st = ''
        st += f"My Name is {self.__name}"
        st += f" - I am {self.__age} years old"
        return st

class Employee(Person):
    em_count = 0
    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.__salary = salary
        Employee.increment_count()

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,value):
        self.__salary = value

    @staticmethod
    def cls_infomation():
        print(f"The infomation of class : ")
        print(f"\t - Class Name : {Employee.__name__}")
        print(f"\t - Base Class : {Employee.__base__}")
        print(f"\t - The Number Employmen: {Employee.em_count}")
        print(f"\t - The Number Person: {Person.count}")

    @classmethod
    def increment_count(cls):
        cls.em_count += 1
    

    def __str__(self):
        return super().__str__() + f" Luong : {self.__salary}"

f = Person("An",23)
k = Person("An",23)
e = Employee("Viet",21,210)
a = Employee("Viet",21,210)
b = Employee("Viet",21,210)
c = Employee("Viet",21,210)

Employee.cls_infomation()
Person.cls_infomation()