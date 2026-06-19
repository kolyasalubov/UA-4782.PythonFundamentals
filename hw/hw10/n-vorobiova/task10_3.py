# TASK 1
class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([width, height, width, height])
        self.width = width
        self.height = height

    def find_area(self):
        return self.width * self.height

print("Завдання 1")
rect = Rectangle(10, 5)
print(f"Площа прямокутника: {rect.find_area()}")
print()

# TASK 2
class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Привіт, {self.name}! Раді тебе бачити.")

    @classmethod
    def get_species(cls):
        return "Homosapiens"

    @staticmethod
    def arbitrary_message():
        return "Це довільне статичне повідомлення, яке не залежить від об'єктів."

print("Завдання 2")
person = Human("Наталія")
person.welcome_message()

print(f"Вид: {Human.get_species()}")
print(Human.arbitrary_message())
print()


# TASK 3:
class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def print_total_employees(cls):
        print(f"Загальна кількість працівників: {cls.employee_count}")

    def display_info(self):
        print(f"Ім'я: {self.name}, Зарплата: {self.salary}")


print("Завдання 3")
emp1 = Employee("Олексій", 25000)
emp2 = Employee("Тетяна", 32000)

emp1.display_info()
emp2.display_info()
Employee.print_total_employees()

print("-" * 30)
print("Базові класи (__bases__):", Employee.__bases__)
print("Простір імен (__dict__):", Employee.__dict__)
print("Назва класу (__name__):", Employee.__name__)
print("Назва модуля (__module__):", Employee.__module__)
print("Документація (__doc__):", Employee.__doc__)