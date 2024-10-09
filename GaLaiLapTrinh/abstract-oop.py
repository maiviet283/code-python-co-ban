from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        self.__age = age

    @staticmethod
    @abstractmethod
    def cls_infomation():
        pass

    @abstractmethod
    @classmethod
    def increment_count(cls):
        pass

    @abstractmethod
    def get_salary(self):
        pass

class Employee(Person):
    em_count = 0
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        self.__salary = value

    @staticmethod
    def cls_infomation():
        print(f"The information of class:")
        print(f"\t - Class Name: {Employee.__name__}")
        print(f"\t - Base Class: {Employee.__base__}")
        print(f"\t - The Number of Employees: {Employee.em_count}")

    @classmethod
    def increment_count(cls):
        cls.em_count += 1

    def get_salary(self):
        return self.__salary
    
e1 = Employee("viet",1,1)
Employee.cls_infomation()