# example1 = "Python is good for everyone"
# print(example1[5])
# print(example1[3:12])
# print(example1[:12])
# print(example1[3:])
# print(example1[:])
# print(example1[:-2])

# example2 = "pythOn is the best"
# print(example2.upper())
# print(example2.lower().upper().title())
# print(example2.title())
# print(example2.strip())
# print(example2.replace('t','o'))
# print(example2.capitalize())
# print(example2.find(' '))
# print(example2.index(' '))

# age = 33
# exp3 = f'My age is {age}'
# print(exp3)
import datetime as dt

# print the datetime format -> 21 Dec 2023 10:00PM (Follow current time)
curDateTime = dt.datetime.now().strftime("%d %m %Y %H:%M%p")
# print the datetime format -> 21/12/2023 10:00:00 (Follow current time)
curDateTime2 = dt.datetime.now().strftime("%x %X")

print(curDateTime)
print(curDateTime2)
# print(curDateTime.weekday())
# print(curDateTime.isoweekday())
# print(curDateTime.isocalendar())
# 2023-12-20

# print the datetime format -> 21 Dec 2023 10:00PM (Follow current time)

## strftime change format ##
## strptime convert data type ##