from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

    @abstractmethod
    def get_salary(self):
        pass

    @classmethod
    @abstractmethod
    def increment_count(cls):
        pass

    @staticmethod
    @abstractmethod
    def cls_information():
        pass

    def __str__(self) -> str:
        return f"{self.__name} ({self.__age})"

class Employee(Person):
    em_count = 0
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary
        Employee.increment_count()

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        self.__salary = value

    @staticmethod
    def cls_information():
        print(f"The information of class:")
        print(f"\t - Class Name: {Employee.__name__}")
        print(f"\t - Base Class: {Employee.__base__}")
        print(f"\t - The Number of Employees: {Employee.em_count}")

    @classmethod
    def increment_count(cls):
        cls.em_count += 1
    
    def get_salary(self):
        return self.__salary

    def __str__(self):
        return super().__str__() + f", Luong: {self.__salary}"

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
    def salary(self, salary):
        self.__salary = salary

    @property
    def bonus(self):
        return self.__bonus
    
    @bonus.setter
    def bonus(self, bonus):
        self.__bonus = bonus

    @classmethod
    def increment_count(cls):
        cls.man_count += 1

    @staticmethod
    def cls_information():
        print(f"The information of class: ")
        print(f"\t - Class Name: {Manager.__name__}")
        print(f"\t - Base Class: {Manager.__base__}")
        print(f"\t - The Number of Managers: {Manager.man_count}")

    def get_salary(self):
        return self.__salary + self.__bonus

    def __str__(self):
        st = super().__str__() 
        st += f" - My Salary is {self.__salary}"
        st += f" - My Bonus is {self.__bonus}"
        return st


mgr1 = Manager("John", 35, 75000, 5000)
mgr2 = Manager("Jane", 40, 80000, 6000)

e1 = Employee("Viet",21,300)
e2 = Employee("Viet",21,300)
e3 = Employee("Viet",21,300)

Employee.cls_information()
Manager.cls_information()

print(mgr1)
print(mgr2)
