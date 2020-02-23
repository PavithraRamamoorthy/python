class Parent():
    def first(self):
        print("this is first function")


class Child(Parent):
    def second(self):
        print("this is second function")

obj = Child()
obj.first()
obj.second()