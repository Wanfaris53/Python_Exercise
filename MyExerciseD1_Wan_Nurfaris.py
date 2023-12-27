        # WAN NURFARIS ISKANDAR BIN WAN AZNAN #

#create a meaningful variable name assign the value Apple to it

fruit = "Apple"
print (fruit)

# #Get user input to display the age category using condition statement
# #0-11 child
# #12-19 teenage
# #20-99 adult

age =int(input("what is your age? "))

if age>=1 and age<12:
    print("you are a child")
elif age>=12 and age<=19:
    print("You are a teenage")
elif age>=20 and age<=99:
    print("You are an adult")
else:
    print("ERROR")


#Exercise3 
#Scenario:Quality control in a Manufacturing Process

voltage =float(input("Input Voltage = "))

if voltage>=0.0 and voltage<3.0:
    print("Low Voltage")
elif voltage>=3.0 and voltage<=3.6:
    print("Standard Voltage")
elif voltage>3.6:
    print("High Voltage")
else:
    print("ERROR VOLTAGE")

#SMALL EXERCISE 4
# Create a calculate BMI function wih the return value method


Weight=float(input("Input Weight in KG = "))
Height=float(input("Input Height in M = "))

def function(Weight, Height):
    return Weight/(Height**2)

print(function(Weight,Height))

# EXERCISE 5
# Create the function for exercise 2

age =int(input("what is your age? "))

def function(age):
    
    if age > 0 and age < 100:
        if age>=1 and age<12:
            return "child"
        elif age>=12 and age<=19:
            return "teenage"
        else:
            return "adult"  
    else:
        print("ERROR")

function(age)
print("you are a ",function(age) )

# # EXERCISE 6
# # Define the function to check if a number is even or ood

num = int(input("Please write a number = "))

def function(num):

    global num_dev    
    num_dev = num % 2
    if num_dev == 1:
        return "an odd number"
    else:
        return "a even number"

function(num)
print("Number",num,"is",function(num_dev))

#exam DP 900
#exam DP 100
