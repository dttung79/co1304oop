from abc import ABC, abstractmethod

class Employee(ABC):
    # class attribute to keep track of total employees
    total_employees = 0
    
    def __init__(self, name):
        self.__name = name
        # set unique ID is incremental based on total employees
        Employee.total_employees += 1
        self.__id = Employee.total_employees

    
    @property
    @abstractmethod
    def salary(self):
        pass

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @property
    def id(self):
        return self.__id
