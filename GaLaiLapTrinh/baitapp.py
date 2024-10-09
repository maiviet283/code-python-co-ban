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

class Manager(Person):
    man_count = 0
    def __init__(self, name, age, salary, bonus):
        super().__init__(name, age)
        self.__salary = salary
        self.__bonus = bonus
        Manager.increment_count()

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def set_salary(self, salary):
        self.__salary = salary

    @property
    def bonus(self):
        return self.__bonus
    
    @bonus.setter
    def set_bonus(self, bonus):
        self.__bonus = bonus

    @classmethod
    def increment_count(cls):
        cls.man_count += 1

    @staticmethod
    def cls_infomation():
        print(f"The information of class: ")
        print(f"\t - Class Name: {Manager.__name__}")
        print(f"\t - Base Class: {Manager.__base__}")
        print(f"\t - The Number of Managers: {Manager.man_count}")
        print(f"\t - The Number of Person: {Person.count}")

    def __str__(self):
        st = super().__str__() 
        st += f" - My Salary is {self.__salary}"
        st += f" - My Bonus is {self.__bonus}"
        return st
    
per1 = Person("Viet",21)
per2 = Person("An",23)
per3 = Person("Viet",21)
per4 = Person("An",23)

mgr1 = Manager("John", 35, 75000, 5000)
mgr2 = Manager("Jane", 40, 80000, 6000)
mgr3 = Manager("John", 35, 75000, 5000)

Manager.cls_infomation()