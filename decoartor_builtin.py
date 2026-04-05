class MyClass:
    @staticmethod
    def hello():
        print("Hello")

class MyClass:
    @classmethod
    def show(cls):
        print(cls)

class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks