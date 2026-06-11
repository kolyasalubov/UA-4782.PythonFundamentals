#1
class Polygon():
    def __init__(self, width, length):
        self.width = width
        self.length = length

class Rectangle(Polygon):
    def get_square_area(self):
        return self.width * self.length

#2
class Human():
    def __init__(self, name):
        self.name = name
    def greeting(self):
        print("Hello " + self.name)
    def get_species(self):
        return "Homosapiens"
    @staticmethod
    def info():
        return "Humans"

#3
class Employee:
    amount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.amount += 1

    @staticmethod
    def print_total_employees():
        print(f"Total employees: {Employee.amount}")

    def info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
print("Class Name (__name__):", Employee.__name__)
print("Base Classes (__base__):", Employee.__base__)
print("Module Name (__module__):", Employee.__module__)
print("Documentation Bar (__doc__):", Employee.__doc__)
print("Class Namespace (__dict__):")
for key, value in Employee.__dict__.items():
    print(f"  {key}: {value}")
