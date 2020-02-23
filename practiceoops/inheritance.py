class Parent():
    def first(self):
       print("this is parent calass")

class Child(Parent):
    def second(self):
       print("this is second class")

obj = Child()
obj.first()
obj.second()