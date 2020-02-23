import re

txt = "pavithra ramamoorthy 1997"
x = re.search("^pavi.*thy$", txt)
if (x):
  print("YES! We have a match!")
else:
  print("No match")

#findall
#set of characters

x=re.findall("[a-m]",txt)
print(x)

#any character
x=re.findall("pa.....a",txt)
print(x)

#does not contain digits
x=re.findall("\D",txt)
print(x)

#contain digits
x = re.findall("\d", txt)
print(x)

#0 or more accrances
x = re.findall("ram*", txt)
print(x)

#one or more
x = re.findall("ram+", txt)
print(x)

#exactly
x = re.findall("mo{2}", txt)
print(x)

#either or
x = re.findall("pavithra|pavi", txt)
print(x)

#biginnng of the string
x = re.findall("\Apavi", txt)
print(x)

#boundry
x = re.findall(r"\bra", txt)
print(x)

x = re.findall(r"\Bra", txt)
print(x)

x = re.findall(r"ra\b", txt)
print(x)

x = re.findall(r"ra\B", txt)
print(x)

#contain space
x=re.findall("\s",txt)
print(x)

#does not contain space
x=re.findall("\S",txt)
print(x)

#contain word
x=re.findall("\w",txt)
print(x)

#does not contain word
x=re.findall("\W",txt)
print(x)

#end of the string
x=re.findall("1997\Z",txt)
print(x)
if(x):
    print("it is match")
else:
    print("it is not match")

#one of the specified character
x = re.findall("[amo]", txt)
print(x)

#lowercase letters
x = re.findall("[a-m]", txt)
print(x)

#[^]
x = re.findall("[^arn]", txt)
print(x)

x = re.findall("[^a-z]", txt)
print(x)

x = re.findall("[0123]", txt)
print(x)

x = re.findall("[0-9]", txt)
print(x)

x = re.findall("[^a-z0-9]", txt)
print(x)

x = re.findall("[0-5][0-9]", txt)
print(x)

x = re.findall("[+]", txt)
print(x)

x = re.findall("[aeiou]", txt)
print(x)

