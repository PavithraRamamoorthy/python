class Parent():
    def func1(self):
        print("this is function 1")
class Child1(Parent):
    def func2(self):
        print("this is the function 2")
class Child2(Child1):
    def func3(self):
        print("this is the function 3")
obj=Child2()
obj.func1()
obj.func2()
obj.func3()