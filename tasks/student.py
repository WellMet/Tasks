"""
This is the 'student' module within the 'tasks' package.
"""

# Classes
class Student:
    def __init__(self, name=None, school=None, age=0):
        self._name = name
        self._school = school
        self._age = age
    @property
    def name(self):
        return self._name
    @property
    def school(self):
        return self._school
    @property
    def age(self):
        return self._age

class Anna(Student):
    def __init__(self):
        super().__init__(name='Anna', school='Folsom High', age=16)
    def say_hello(self):
        msg = "Hello, my name is {} and I am from {}".format(self.name, self.school)
        print(msg)

class Luke(Student):
    def __init__(self):
        super().__init__(name='Luke', school='Folsom High', age=17)
    def say_hello(self):
        msg = "Hello, my name is {} and I am from {}".format(self.name, self.school)
        print(msg)

class Sheldon(Student):
    def __init__(self):
        super().__init__(name='Sheldon', school='Intel High', age=25)
    def say_hello(self):
        msg = "Hello, my name is {} and I am from {}".format(self.name, self.school)
        print(msg)