def is_even(n):
    return n%2==0
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
evens=list(filter(is_even,nums))
print(evens)

#using lambda

nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
evens=list(filter(lambda n:n%2==0,nums))
print("The list of even numbers is:",evens)