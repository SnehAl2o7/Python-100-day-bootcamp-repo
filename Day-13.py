from Data import data
import random

def format(account):
    """Format the account data into a printable format."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"Name: {name}\nDescription: {description}\nCountry: {country}"

def answer(guess, a_follower, b_follower):
    """Check if the user's guess is correct."""
    if a_follower > b_follower:
        return guess.lower() == 'a'
    else:
        return guess.lower() == 'b'

score = 0
game_end = True

account_b = random.choice(data)

while game_end:
    
    account_a = account_b
    account_b = random.choice(data)
    
    # Ensure account_b is different from account_a
    while account_a["name"] == account_b["name"]:
        account_b = random.choice(data)

    print(f"Compare A:\n{format(account_a)}.")
    print(f"Compare B:\n{format(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]

    is_correct = answer(guess, a_follower, b_follower)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_end = False 
        print(f"Sorry, that's incorrect. Final score: {score}")