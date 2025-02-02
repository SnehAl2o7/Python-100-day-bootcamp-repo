# #PROJECT NO - 5
# #PRACTICE NO-1
# #USING FOR LOOP
# fruits = ["apple","peach","pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "pie")

# #PRACTICE NO-2 #AVERAGE HEIGHT
# student_height = [180, 124,165,173,189,169,146]
# total, cnt = 0,0
# for height in student_height: # also use total = sum(student_height)
#     total += height
#     cnt += 1 # for length, use len(student_height)
# print("The average height is: ", int(total/cnt))

# #PRACTICE NO-3 #HIGHEST SCORE
# student_scores = [78, 65, 89, 91, 85, 88] #can also use max() function
# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score

# print("The highest score is: ", max_score)

# #PRACTICE NO-4 
# total = 0
# for i in range(1,101):
#     total += i
# print(total)

# #adding even
# eventotal = 0
# for i in range(1,101,2):
#     eventotal += i
# print(eventotal)

# #PRACTICE NO-5 #FIZZ BUZZ CHALLENGE
# for i in range(1,101):
#     if(i %3 == 0 and i%5 == 0):
#         print("FizzBuzz")
#     elif(i %3 == 0):
#         print("Fizz")
#     elif(i%5 == 0):
#         print("Buzz")
#     else:
#         print(i)

#PROJECT NUMBER-5
import random
print("Welcome to the PyPassword Generator!")
len = int(input("How many letters would you like in your password?\n"))
sym = int(input("How many symbols would you like?\n"))
num = int(input("How many numbers would you like?\n"))

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
password = ""

word = []
for i in range(len):
    word.append(random.choice(letters))
    if(i < num):
        word.append(random.choice(numbers))
    if(i < sym):
        word.append(random.choice(special))

for i in word:
    ch = random.choice(word)
    password += ch

print("Here is your password: ", password)
