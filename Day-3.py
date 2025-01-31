#PROJECT NO -3

#PRACTICE -1
#Syntax
# if condition:
#     statement
# else:
#     statement
print("Welcome to the Roller roaster")
height = int(input("What is your height:"))
if height >= 120:
    print("You can ride the roller coaster!")
else:
    print("You are not tall enough to ride the roller coaster!")

#PRACTICE NO-2 (ODD AND EVEN)
num = int(input("Enter a number:"))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# syntax for nested and elif condition
# if condition: statement
# elif condition: statement
# else : statement

# if condition:
#     if condition:
#         statement1
#     else:
#         statement2
# else:
#     statement3

#PRACTICE NO-4
height = input("enter your height in metre")
weight = input("enter your weight in kg")
BMI = int(weight) / (height ** 2)
if BMI < 18.5:
    print("You are underweight")
elif 18.5 <= BMI < 25:
    print("Your are is normal")
else :
    print("You are overweight")

#PRACTICE NO-5


#PROJECT NUMBER- 3
print("Welcome to Treasure Island.")
print("Your mission is to find the hidden treasure.")
print("You cross roads with e")
choice = input("Do you want to go left or right?").lower()
if choice == "left":
    choice = input("Do you want to go left or right?").lower()
    if choice == "right":
        print("Game Over")
    else:
        print("You found the treasure!")
else:
    print("Game Over")



