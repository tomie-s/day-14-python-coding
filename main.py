#TIP 1 - Import the logo and vs from art.py
import random
from replit import clear
from art import logo, vs
from game_data import data

#format data
def format_data(choice):
    name = choice["name"]
    desc = choice["description"]
    country = choice["country"]
    return f"{name}, a {desc}, from {country}."

#TIP 3 - Create a function that compares the follower count of the 2 choices.
def compare_followers(account_A, account_B):
    if account_A['follower_count'] > account_B['follower_count']:
        return account_A
    else:
        return account_B

#TIP 4 - Make a function to compare user's guess with higher_follower variable. 
def compare_guess(user_choice, higher_followers):
    return user_choice["name"] == higher_followers["name"]

#TIP 5 - Create a while loop that continues if user is right.
print(logo)
play_game = True
user_score = 0

#TIP 2 - Create 2 random choices from game_data in function. Save them in variables.
choice_B = random.choice(data)

while play_game:
    choice_A = choice_B
    choice_B = random.choice(data)
    
    while choice_A == choice_B:
        choice_B = random.choice(data)
    
    
    if user_score >= 1:
        print(f"You're right! Current score: {user_score}")
        
    print(f"Compare A: {format_data(choice_A)}")

    print(vs)
    print(f"Against B: {format_data(choice_B)}")

    higher_followers = compare_followers(choice_A, choice_B)

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    user_choice = choice_A if guess == 'a' else choice_B
    
    #TIP 6 - If user is right, update user_score and continue the game. If user is wrong it should end the game.
    clear()
    print(logo)
    
    if compare_guess(user_choice, higher_followers):
        user_score += 1
    else:
        play_game = False
        print(f"Sorry, that's wrong. Final score: {user_score}")
