from random import randint

easy_level=10
hard_level=5

def check_answer(guess,answer,turns):
    if guess> answer:
        print("too high")
        return turns -1
    elif guess < answer:
        print ("too low")
        return turns -1
    else:
        print(f"you have guessed it right, the answer is: {answer}")

def level():
    difficulty= input("Choose you difficulty level , 'easy' or 'hard': ")
    if difficulty=='easy':
        return easy_level
    else:
        return hard_level


def game():
    print("Welcome to number guessing game.")
    print (" I am thinkning a number between one and hundred")
    answer = randint(1,100)
    turns = level()
    guess = 0
    while guess!=answer:

        print(f"You have {turns} attempts left")
        guess =int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)
        if turns ==0:
            print("You have run out guesses, you lose")
            print(answer)
            return
        elif guess!= answer:
            print("Guess again")

game()