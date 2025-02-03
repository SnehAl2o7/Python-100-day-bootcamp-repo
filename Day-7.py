#PROJECT NUMBER -7
#PRACTICE NO - 1
import random
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# guess = input("guess a letter:").lower()
# for ch in chosen_word:
#     if ch == guess:
#         print("right")
#     else:
#         print("wrong")

#PRACTICE NO - 2
# word_list = ["apple","mango","Orange"]
# chosen_word = random.choice(word_list)
# print("Passt is ",chosen_word)
# display = []
# guess = input("Enter a letter:").lower()
# for i in chosen_word:
#     if(i == guess):
#         display += i
#     else:
#         display += "_"
# print(display)

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




