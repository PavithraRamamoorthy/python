#reading file#
f=open("class1.py")
print(f.readline())
print(f.read())
print(f.readlines())


"""file input template"""
input=open("class1.py")
for line in input:
    print(line.strip())




