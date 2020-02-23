class Parent():
    def function1(self):
        print("this is the first function")
class Child1(Parent):
    def function2(self):
        print("this is the second function")
class Child2(Parent):
    def function3(self):
        print("this is the 3 function")

obj=Child1()
obj1=Child2()
obj.function1()
obj.function2()