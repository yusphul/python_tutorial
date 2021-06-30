import keyword
print("HMMM... Another banger (:")
name = "Tunde"
age = 23
pi = 3.21
isAdult = True
listOfNumber = []

"""
This is just
for Multi-line comment
"""
#Checking datatype of Variables in Python

print("Checking datatype of Variables in Python")
print("====================================")
print()
print(type(name))
print(type(age))
print(type(pi))
print(type(isAdult))
print(type(listOfNumber))

# Counting lenght of a String
myName = "Yusuf Adejumo"
print(len(myName))

# Replacing
print(myName.replace("Y", "T"))

# Checking if a phrase is in a string
if ("ade" in myName):
    print("O wa ni be")
else:
    print("error")

career1 = "DevOps"
career2 = "SRE"
comment = f"""
Hey {myName}
How are you doing today?
You're {4+24}years old, I believe you've decided of the next career path for to follow"
{career1} & {career2} is the way. Good luck and see you at the top
"""
print(comment)

# List of reserve keywords in Python
print(keyword.kwlist)
print()
print()
operator =f"""
Arithemtic Operation
====================
*
** -> Raise to power
-
+
%

Comparism Operator
==================
<
<=
>
>=
!=
==

Logical Operators
=================
AND
OR
"""
print("Below is the list of Python Operator")
print(operator)



print("Ternery IF statement in python. This is preferrably use when you have IF Else. It ained at shortten the line of code")
print("============================")

"""
number= -1
if number>0:
    print(f"Hey, number is greater than zero. Actually it's {number}")
else:
    print(f"{number} is less than zero")
"""

#Converting the above code in Ternery IF Statement
number= 10
message = f"{number}, positive" if number>0 else f"{number} is less than zero"
print(message)

print()
# Dealing with LIST
print("Dealing with LIST")
myList = [1,2,3,4.4,["A","B","Jack",24]]
print(myList[4][2])

#myList.sort()
#print(myList)
print(len(myList))

myList.reverse()
print(myList)




def wordcount():
    my_string ="Please enter your  bhjggjhgjh ghghjkg jklsentence"
    count=0

    for i in range(len(my_string)):
        if my_string[i] != '':
            count += 1

        else:
            print("Empty sentence")
    print(f"The total number of character in the sentence is {count}")

    #print(my_string)

wordcount()

def numbercounter():
    number =123
    my_array = [1, 2, 3, 1, 5, 6 ]
    mystring = "This is anpther good day, my people"
    counter = 0

    for i in range(len(my_array)):
        if my_array[i] != '':
            counter +=1
        else:
            print("I can't find anything")

    print(f"Total numner of element is {counter}")

numbercounter()

print("pushing to Git")


"""
#SET Union, interception and difference
In python, the foloowing symbols are use to 
Union = | (Pipe)
Interception = & (Ampersand)
Difference = _ (Minus)

"""



lettersA = {"A","B","C","G","H"}
lettersB = {"D","B","A","G"}
union = lettersA | lettersB
intercept = lettersA | lettersB
difference = lettersA - lettersB
print(f"The union add distinct value of the variables together. The output is the arranged because the data type of the variables are SET Union is {union}")
print(f"Interception for the set = {intercept}")
print(f"Interception for the set = {difference}")


#Count the number of character in a sentence
def character_counter():

    sentence = "This is another good day, keep learning and you will hit your goals shortly."
    counter=0
    for i in range(len(sentence)):
        if sentence[i] != '':
            counter +=1
    print(f"The total caharater is {counter}")

character_counter() 