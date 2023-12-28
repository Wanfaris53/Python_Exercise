# Exercise 1
# Add loop and interation for day 1 Exercise 5
# and stop when don't want to ask the age


# def function(age):
    
#     if age > 0 and age < 100:
#         if age>=1 and age<12:
#             return "child"
#         elif age>=12 and age<=19:
#             return "teenage"
#         else:
#             return "adult"  
#     else:
#         print("ERROR")
# ask = "y"

# while ask == "y":
#     age =int(input("what is your age? "))
#     function(age)
#     print("you are a ",function(age) )
#     ask = input("Do you want to ask again (y/n)? ")
# else:
#     print("Done")


# Exercise 2
# Print the multiplication table for the number 1 to 10 with int input
    
# num = int(input("Enter a number = "))

# def function(num):
#     num = num * x
#     return num

# for x in range(1,11):    
#     print(num, "x",x,"=",function(num))

# Exercise 3
# Write a small program about the order food menu
    
# Display Menu
# User input (in loop)
# Calculation
# Display total
## Condition statement
## Function
## f string

menu = '''
                     ----MENU----
        FOOD             CODE                    PRICE
    * NASI AYAM          (NA)       ->         RM 6.00
    * NASI AYAM PENYET   (NAP)      ->         RM 7.50
    * BAKSO              (B)        ->         RM 6.00
    * BIHUN SUP          (BS)       ->         RM 6.50'''
print(menu)

NA = 6.00
NAP = 6.50
B = 6.00
BS = 6.50

def calculate(code,tot):

    if code == "NA":
        price = NA * tot
    elif code == "NAP":
        price = NAP * tot
        return price
    elif code == "B":
        price = B * tot
        return price
    elif code == "BS":
        price = BS * tot
        return price
    else:
        return price

ask = "Y"
final_total = 0
final_tot = 0

while ask == "Y":
    total = 0.00
    code = input("What would you like to order? ")
    while code != "B" and code != "NA" and code != "NAP" and code != "BS":
        code = input("What would you like to order? ")
    else:
        tot = float(input("How much do you want? "))
    total = calculate(code,tot)
    final_total = final_total + total
    final_tot = final_tot + tot
    print("Your current total item is",int(final_tot))
    print("your current total price is RM",final_total)
    ask = input("Do you to add another order (Y/N)? ")
else:

    if final_total > 100:
        final_total = final_total * (0.90)
        print("You order more then RM100, You got 10% /discount")
        print("Thank you for the purchase, please wait for a while, our chef is preparing your order")
        print(f"Your total item is ",int(final_tot))
        print(f"Your total price is RM",(final_total))
    else:
        print("Thank you for the purchase, please wait for a while, our chef is preparing your order")
        print(f"Your total item is ",int(final_tot))
        print(f"Your total price is RM",(final_total))






