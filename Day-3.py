
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
print("Welcome to the Love calculator")
name1 = input("What is your name: \n")
name2 = input("What is their name: \n")
combined_str = name1+name2
lower = combined_str.lower()
t = lower.count('t')
r = lower.count('r')
u = lower.count('u')
e = lower.count('e')
true = t+r+u+e
l = lower.count('l')
o = lower.count('o')
v = lower.count('v')
e = lower.count('e')
love = l+o+v+e
love_score = int(str(true) + str(love))
if(love_score < 0) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos")
elif(love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, you are alright together")
else:
    print(f"Your love score is {love_score}") 


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


