#PROJECT NUMBER - 12
#Python only follow global and local scope , for functions not in
# loops and if statement

#Global scope
enemies = 1

def increase():
    global enemies #accessing global scope
    enemies += 1
    print(f" Enenies inside function: {enemies}")

increase()
print(f"Enemies outside function: {enemies}")

#Python constant and global scope
#Project
import random
def check(attempt,num,):
    while(attempt != 0):
        print(f"You have {attempt} attempts remaining to guess the number")
        guess = int(input("Make a guess : "))
        if(guess == num):
            print(f"Yay! You have guessed the number {num} correctly")
            break
        elif(guess > num):
            print("Too high!\n Guess again")
        else:
            print("Too low!\n Guess again")
        attempt -= 1
    if attempt > 0:
        print(f"You got it! The answer was {num}")
    else:
        print(f"Game over! You are out of guess. The answer was {num}")

def set_difficulty():
    num = random.randint(1,100)
    level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if level == "easy":
        attempt = 10
        check(attempt,num)
    
    elif level == "hard":
        attempt = 5
        check(attempt,num)


print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
set_difficulty()



    