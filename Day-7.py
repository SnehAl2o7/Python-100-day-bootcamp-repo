#PROJECT NUMBER -7
#PRACTICE NO - 1
import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
guess = input("guess a letter:").lower()
for ch in chosen_word:
    if ch == guess:
        print("right")
    else:
        print("wrong")

#PRACTICE NO - 2
word_list = ["apple","mango","Orange"]
chosen_word = random.choice(word_list)
print("Passt is ",chosen_word)
display = []
guess = input("Enter a letter:").lower()
for i in chosen_word:
    if(i == guess):
        display += i
    else:
        display += "_"
print(display)

#PRACTICE NO - 3
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f"Psst, the solution is {chosen_word}.")
display = ["_"] * word_length
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for i in range(word_length):
        if(chosen_word[i] == guess):
            display[i] = guess       
    print(display)
    if '_' not in display:
        end_of_game = True
    print("You win")

#PROJECT NUMBER - 4 HANGMAN

from hangman_words import word_list
from hangman_image import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(logo)

print(f"Psst, the solution is {chosen_word}.")
display = ["_"] * word_length
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed the letter {guess}.")
    for i in range(word_length):
        if(chosen_word[i] == guess):
            display[i] = guess   
           
    if guess not in chosen_word:
        lives -= 1
        print(f"You have {lives} lives left.")
        print(f"The word {guess} you guessed is not in the word.")
        if lives == 0:
            print("You lose")
            end_of_game = True
    print(display)
    
    if '_' not in display:
        end_of_game = True
        print("You win")
    print(stages[lives])
