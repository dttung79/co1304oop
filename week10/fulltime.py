from employee import Employee

class FullTime(Employee):
    def __init__(self, name, rate):
        # call the parent constructor to initialize name and id
        super().__init__(name)
        # set the rate
        self.__rate = rate

    # overriding the abstract property salary
    @property
    def salary(self):
        return self.__rate * 1000
    
    @property
    def rate(self):
        return self.__rate
    
    @rate.setter
    def rate(self, new_rate):
        self.__rate = new_rate

if __name__ == "__main__":
    john = FullTime("John Doe", 2.5)
    print(f"Employee ID: {john.id}, Name: {john.name}, Salary: {john.salary}")
    paul = FullTime("Paul Smith", 3.0)
    print(f"Employee ID: {paul.id}, Name: {paul.name}, Salary: {paul.salary}")