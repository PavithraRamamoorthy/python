name="pavithraramamoorthy"
print(name.upper())
print(name.lower().startswith("pa"))
print(len(name))



#spliting string#
name="i am pavithra rangineni"
for word in name.split():
    print(word)

#joining string#

name="pavithra is a BSC(c.s) student"
print ("MCA".join(name.split("BSC(c.s)")))

#spliting into variables#

str="pavithra 22 567.23"
name,age,money=str.split()
print(name)
print(age)
print(money)

#writing files#
f=open("class1.py")
f.write("hello, world!\n")
