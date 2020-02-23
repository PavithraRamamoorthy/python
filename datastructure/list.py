# add values to list
for number in range( 1,11):
    aList=[]
    aList += [ number ]
    print ("The value of aList is:", aList)

# access list values by iteration
print ("\nAccessing values by iteration:")
for item in aList:
  print (item, end=" ")

# access list values by index
print("\nAccessing values by index:")
print("Subscript Value")
for i in range(len(aList)):
      print("%9d %7d" %(i, aList[i]))

# modify list
print ("\nModifying a list value...")
print ("Value of aList before modification:", aList)
aList[ 0 ] = -100
aList[ -3 ] = 10
print ("Value of aList after modification:", aList)
print(aList)
