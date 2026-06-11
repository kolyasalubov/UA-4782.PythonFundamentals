#1
class Ball():
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type
#2
import random

class Ghost:
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)
#3
class Human():
    def __init__(self):
        species = "Human"

    @staticmethod
    def creation():
        return Man(), Woman()

class Man(Human):
    def __init__(self):
        Human.__init__(self)

class Woman(Human):
    def __init__(self):
        Human.__init__(self)
#4
class Person():
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.info=f"{name}s age is {age}"
    def info_getter(self):
        return self.info

#5
import math

class Sphere(object):
    def __init__(self, radius: float, mass: float):
        self.radius = radius
        self.mass = mass
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        return round(4/3 * self.radius ** 3 * math.pi, 5)
    def get_surface_area(self):
        return round(4 * self.radius ** 2 * math.pi, 5)
    def get_density(self):
        return round(self.mass / self.get_volume(), 5)
#6
class MyClass:
    @staticmethod
    def class_name_changer(cls, new_name):
        if not new_name or not new_name[0].isupper() or not new_name.isalnum():
            raise ValueError("Invalid class name! Must be alphanumeric and start with an uppercase letter.")
        cls.__name__ = new_name
