class Person:
    def method1(self):
        print("pavithra")

    def method2(self, somestring):
        print("python Testing:" + somestring)

def main():

    str = Person()
    str.method1()
    str.method2("Welcome to python")

if __name__ == "__main__":
    main()