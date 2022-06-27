import random
import os


from requests import get
from game_data import data

def get_random_acc():
    return random.choice(data)

def format_data(account):
    name=account["name"]
    description=account["description"]
    country =account["country"]
    return f"{name}, a {description}, from {country}"

def right_answer(guess,a_followers,b_followers):
    if a_followers > b_followers:
        return guess=="a"
    else:
        return guess=="b"

def game():
    score =0
    game_should_continue=True
    acc_a= get_random_acc()
    acc_b= get_random_acc()

    
    while game_should_continue:
        acc_a = acc_b
        acc_b= get_random_acc()
    
        while acc_a == acc_b:
            acc_b= get_random_acc()
        
        print(f"Compare A: {format_data(acc_a)}")
        print(f"Compare B:{format_data(acc_b)}")

        guess=input("Who has more followers? Type 'a' or 'b' ").lower()
        a_follower_coumt= acc_a["follower_count"]
        b_follower_count=acc_b["follower_count"]
        is_correct = right_answer(guess,a_follower_coumt,b_follower_count)
        os.system('cls||clear')
        if is_correct:
            score+=1
            print(f"you are right! current score:{score}, ")
        else:
            game_should_continue=False
            print(f"sorry, thats wrong. Final score:{score}. ")



game()