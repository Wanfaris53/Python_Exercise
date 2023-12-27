#Wan Nurfaris

#print("Hello")

# x = 5
# y = 6.333333333333333
# c = "john"
# print(x,y,c)

# x = 12.32
# y = 2
# z = x + y
# if z > y:
#     print(z, "is greater then" ,y)

# var_char = "dad"
# varchar = "faris"
# VarChar = "wan"
# print(var_char ,varchar ,VarChar)

# Y = 5
# a = float(Y)
# print (Y,a)

#input random number

# import random
# print(random.randrange(1,10))


# a = 5
# a += 4
# # same as a = a + 4
# print(a)

# print (1 == 10)
# print (1 != 10)
# print (1 > 10)
# print (1 < 10)

#logical operator

# x = 10
# print (x > 3 and x < 20)
# print (x > 3 and x > 20)
# print (x > 3 or x > 20)
# print (not(x > 3 and x > 20))

#if else

# x = 16
# y = 13

# if x > y :
#     print(x," more then ", y)
# elif x < y :
#     print (x, " less then ",y)
# else:
#     print("X and Y is the same number")

# print("What is your name?")
# username = input()
# usernames = ''.join(filter(lambda x: not x.isdigit(), username))
# print ("Hi "+ str(usernames))

# print("What is your name?")
# username = input()
# if username.isalpha():
#     print("Hi "+ username)
# else:
#     print("Invalid")

##FUNCTION##

# def function():
#     print("Hi")
# function()

# def function(fname, lname):
#     print(fname , lname)

# function("Wan", "Aznan")
# function("Iskandar", "Faris")
# function("Nur", "Faris")

##ARBITRARY ARGUMENTS##
# if the urgument number is unknown, use *
# def function(*fname):
#     print("The winner is", fname[2])

# function("faris","iskandar","wan","nurfaris")

##KEYWORD ARGUMENT##
# def function(fname, mname, lname):
#     print("Wow name :", lname)

# function(fname="Wan",mname="faris", lname="iskandar")

# ##abitrary keyword arguments (if the argument number is unknown)
# # use ** to receive dictionary arguments
# def function(**people):
#     print("Wow name :", people["lname"])

# function(fname="Wan",mname="Faris", lname="Iskandar")

# def function(country ="Malaysia"):
#     print("I come from", country)

# function("Singapure")
# function()
# function("Indonesia")

# def function(x):
#     return 10 * x

# print(function(9))
# print(function(2))

x = "batman"

def function():
    x = "ironman"
    print("I'm", x)

function()
print("I'm", x)
