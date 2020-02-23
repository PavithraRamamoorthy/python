#1#
nums=[0, 4, 7, 2, 1, 0 , 9 , 3, 5, 6, 8, 0, 3]
evens=list(map(lambda x  :x % 5 ,nums ))
print(evens)

#2#
str = ['once', 'upon', 'a', 'time', 'in', 'a']
def foo (x):
  return x * 3
bar = foo
change=list(map (foo, str))
change1=list(map (bar, str))
print(change)
print(change1)

#3#
nums=list(map(lambda x : x*x*x,range(1,5)))
print(nums)

#4#
nums=list(map(lambda x:x*2,[1,2,3,4,5,6,7,8,9,10]))
print(nums)
