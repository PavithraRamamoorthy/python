def f(x):
    return x % 2 !=0 and x % 3 !=0
nums=list(filter(f,range(1,11)))
print(nums)

#using lambda#
nums=list(filter(lambda x: x % 2 !=0 and x % 3 !=0,range(1,11)))
print(nums)