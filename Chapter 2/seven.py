def sumTo(n):
   
    list_of_all_integers = range(0, n+1)
   
    return sum(list_of_all_integers)

from test import testEqual

def sumTo(n):
    result = (n * (n + 1)) / 2
    return result

# Now lets see how well this works
t = sumTo(0)
print("The sum from 1 to 0 is",t)
t = sumTo(10)
print("The sum from 1 to 10 is",t)
t = sumTo(5)
print("The sum from 1 to 5 is",t)