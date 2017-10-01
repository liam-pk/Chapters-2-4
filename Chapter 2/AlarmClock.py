n = int(input("Enter the number of hours: "))
days = n // 24
timeafter = n % 24
if (timeafter > 10):
days = days + 1
hours = timeafter - 10
else:
hours = timeafter + 14

print("End time is in: ", days, " days, at ", hours, ":00 hours")
