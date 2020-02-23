class Parent1():
    def function1(self):
        print("this is first function")
class Parent2():
    def function2(self):
        print("this is second function ")
class Child(Parent1,Parent2):
    def function3(self):
        print("this is funtion 3")
obj=Child()
obj.function1()
obj.function2()
obj.function3()