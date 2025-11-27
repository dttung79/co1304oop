from fulltime import FullTime

class DailyPartTime(FullTime):
    def __init__(self, name, rate, days):
        # call the parent constructor to initialize name and rate
        super().__init__(name, rate)
        # set the number of working days per week
        self.__days = days
    
    # overriding the salary property to calculate based on days worked
    @property
    def salary(self):
        return self.rate * 1000 * self.__days / 5
    
    @property
    def days(self):
        return self.__days
    
    @days.setter
    def days(self, new_days):
        self.__days = new_days

if __name__ == "__main__":
    john = FullTime("John Doe", 2.5)
    print(f"Employee ID: {john.id}, Name: {john.name}, Salary: {john.salary}")
    paul = DailyPartTime("Paul Smith", 2.5, 2)
    print(f"Employee ID: {paul.id}, Name: {paul.name}, Salary: {paul.salary}")