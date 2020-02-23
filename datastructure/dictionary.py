# Creating, accessing and modifying a dictionary.
# create and print an empty dictionary
emptyDictionary = {}
print ("The value of emptyDictionary is:", emptyDictionary )

# create and print a dictionary with initial values
grades = { "pavi": 87, "divya": 90, "kaviya": 92, "kokila": 95 }
print ("\nAll grades:", grades )

# access and modify an existing dictionary
print ("\ndivya's current grade:", grades[ "divya" ] )
grades[ "divya" ] = 89
print ("divya's new grade:", grades[ "divya" ] )

# add to an existing dictionary
grades[ "nithya" ] = 93
print ("\nDictionary grades after modification:" )
print (grades )

# delete entry from dictionary
del grades[ "pavi" ]
print ("\nDictionary grades after deletion:" )
print (grades)



#dictionary methods
monthsDictionary = { 1 : "January", 2 : "February", 3 : "March",
4 : "April", 5 : "May", 6 : "June", 7 : "July",
8 : "August", 9 : "September", 10 : "October",
11 : "November", 12 : "December" }
print ("The dictionary items are:")
print (monthsDictionary.items() )
print ( "\nThe dictionary keys are:")
print ( monthsDictionary.keys() )
print ("\nThe dictionary values are:")
print (monthsDictionary.values() )
print ("\nUsing a for loop to get dictionary items:")
for key in monthsDictionary.keys():
  print ("monthsDictionary[", key, "] =", monthsDictionary[key])
