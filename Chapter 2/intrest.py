P = 10000 
r = 8/100 
n = 12
t = int(input("Please enter the number of years to save for: "))

A = P * (1 + r/n)**(n*t)

print("Your final amount is: ", A)