## FILE HANDLING ##

# file = open("D4KISMEC.txt","r")
# # file = open("D4KISMEC.txt","a")
# # file.write("\n dehhhhhhhhhhhhh")

# file = open("D4KISMEC.txt","w")
# file.write("KISMEC hacked this text file ")
# file = open("D4KISMEC.txt","r")
# print(file.read())

# file.close()

# file = open("KISMEC3.txt","w")
# file.write("suiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")

# import os

# if os.path.exists("KISMEC3.txt"):
#     os.remove("KISMEC3.txt")
#     print("Dah delete")
# else:
#     print("Dah delete sebelum ni")

## ARRAY ##
    ## LIST ##    
prog_lang = ['python','C++','C', 'java','R']

print(prog_lang)

num_list = [1,2,3,4,5,6]
bool_list = [True,False,True,False,True,False,True]

mix_list = [ 'python',1,True]
print(mix_list)

os_list = list(('Windows','Linux', 'Mac'))
print(os_list)

print(type(os_list))

## HOW TO TAKE OUT SOME DATA IN THE LIST ##

print(prog_lang[0:3])
print(prog_lang[-3:])

## CHECK ITEM ##

if 'pythonx' in prog_lang:
    print("ada")
else:
    print("takde")

## CHANGE ITEM ##

prog_lang[4] = 'jupyters'
print(prog_lang)

prog_lang[2:4] = ['jupyter, ruby']
print(prog_lang)

## ADD LIST ##

prog_lang.insert(0, 'ruby')
print(prog_lang)

## APPEND ##

prog_lang.append('CSS')
print(prog_lang)

## EXTEND ##

mobileOS = ['Android', 'IOS','WindowsOS']

os_list.extend(mobileOS)
print(os_list)

## TUPLE ##

os_tuple = ('Unix', 'chrome')

os_list.extend(os_tuple)
print(os_list)

# os_tuple.remove('Unix')
# print(os_tuple)

prog_lang.pop(2)
print(prog_lang)

prog_lang.pop()
print(prog_lang)

## DELETE ##

del prog_lang[0]
    # del prog_lang[] ## this will delete the list
print(prog_lang)

    # prog_lang.clear ## will clear all the data in the list

 ## LOOP ##
for x in os_list:
    print(x)
 ## RANGE ##
for x in range(len(os_list)):
    print(os_list[x])

x = 0
while x < len(os_list):
    print(os_list[x])
    x += 1 

## Loop using list comprehension
    
[print(x) for x in os_list]

newlist = []

for x in os_list:
    if 'W' in x:
        newlist.append(x)

print(newlist)

newlist2 = [x for x in os_list if 'W' in x]
print(newlist2)

## SORTING ##

## ASCENDING ##

os_list.sort()
print(os_list)

print(num_list)
num_list2 = [100,54,663,6969, 53,5533]
print(num_list2)
num_list2.sort()
print(num_list2)

num_list.sort(reverse=True)
print(num_list)

os_list.sort(reverse=True)
print(os_list)

## CUSTOMIZE SORT ##

os_list.sort(key= str.lower)
print(os_list)

os_list.sort(key= len)
print(os_list)

def count_vowel(x):
    vowels = 'aeiouAEIOU'
    sum = 0
    for char in x:
        if char in vowels:
            sum =sum + 1
    return sum

os_list.sort(key=count_vowel)
print(os_list)

## REVERSE ##

os_list.reverse()
print(os_list)

## COPY LIST ##

mylist = list(os_list)
print(mylist)

## JOIN LIST ##
mylist = ['Machine Learning','Deep Learning', 'AI']
marklist = [90,80,70]

joinlist = mylist + marklist
print(joinlist)