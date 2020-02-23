from functools import reduce

def add_all(a,b):
    return a+b

nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)
doubles=list(map(lambda n:n*2,nums))
print(doubles)

sum=reduce(add_all,doubles)
print(sum)

#reduce using lambda
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)
doubles=list(map(lambda n:n*2,nums))
print(doubles)

sum=reduce(lambda a,b:a+b,doubles)
print(sum)
