fhand = open('class1.py')
print(fhand.readlines())
print(fhand.readlines())



specific_line_number=5
fhand = open('class1.py')
all_lines_variable = fhand.readlines()
print(all_lines_variable[specific_line_number -1])