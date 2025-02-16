#PROJECT NUMBER - 11
#BLACK JACK
import random
card = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    return random.choice(card)

def calculate_score(list):
    total = sum(list)
    if total == 21 and len(list) == 2:
        return 0
    if total == 21:
        return 0
    if total > 21 and 11 in list:
        total -= 10;
    return total

is_game_over = True

def compare(user,dealer):
    if user == dealer:
        return "It's a draw"
    elif user == 0:
        return "Lucky! You got a blackjack, You win"
    elif dealer == 0:
        return "Unlucky! Dealer got a blackjack, You lose"
    elif user > 21:
        return "You went over! You lose"
    elif dealer > 21:
        return "Dealer went over! You win"
    elif user > dealer:
        return "You win"
    else:
        return "You lose"

user_card = []
dealer_card = []

for i in range(2):
        user_card.append(deal_card())
        dealer_card.append(deal_card())

user = calculate_score(user_card)
dealer = calculate_score(dealer_card)

while(is_game_over):
    
    user = calculate_score(user_card)
    dealer = calculate_score(dealer_card)
    print(f"Your cards: {user_card}, current score: {user}")
    print(f" Computer's first card: {dealer_card[0]}")

    if user == 0 or dealer == 0 or user > 21 or dealer > 21:
        is_game_over = False
    else:
        deal = input("Type  'H' to draw another card, type 'S' to stop drawing cards: ")
        if deal.upper() == "H":
            user_card.append(deal_card())
        else :
            is_game_over = False

while dealer != 0 and dealer < 17:
    dealer_card.append(deal_card())
    dealer = calculate_score(dealer_card)

print(compare(user,dealer))