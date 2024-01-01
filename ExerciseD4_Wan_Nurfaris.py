# Day 4 Exercise 1
# 1. User input (ask birthday date)
# 2. Calculate the age of the user
# 3. Save the information to the file and read the file
# Main method: Date and time function and file handling

import datetime as dt
import datetime as date_


date = input( "What is your birthday (12 03 1234) = ")

date = dt.datetime.strptime(date,"%d %m %Y")

print(date)
date = date.year

# datenow = date_.datetime.now().strptime("%d %m %Y")
datenow = date_.datetime.now().year
print(datenow)

age = datenow - date

print(age)

file = open("birthday.txt","w")
file.write(f'your age is {age}')

file.close()