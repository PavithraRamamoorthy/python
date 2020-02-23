def c_to_f(c):
    print (c_to_f)
    return c / 5.0 * 9 + 32

def make_message(temp):
    print (make_message)
    return str(temp)

for tempc in [19,22,21]:
    tempf = c_to_f(tempc)
    message = make_message(tempf)
print (message)
