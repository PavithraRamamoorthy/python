fname = raw_input("class1.py")
fhand = open("class1.py")
count = 0
for line in fhand:
 if line.startswith("person:") :
  count = count + 1
print ("There were", count, "subject lines in", class1.py)