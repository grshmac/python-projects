#random module in python
import random

# num= random.randint(1,10)
# print(num)
# word= random.choice(["sun","moon","gay","love"])
# print(word)
# print(f'I love {word} {num} time(s)')

#1. let's practise the guess the num with python choosing the number first
def random_num(x):
    # guess=int(input("Guess the no btwn 9-24:"))
    rand= random.randint(9,x)
    guess = 0
    while guess != rand :
        guess = int(input(f"Guess the no btwn 9-{x}:"))
        if guess> rand:
            print("Its high")
        elif guess<rand:
            print("Its low")
    print("You guessed correct!")

random_num(100)

#2. let's now practise the guess the num with user choosing the number first
def computer_guess(x):
    low=0
    high=x
    reply=''
    while reply != 'c':
        guess= random.randint(low,high)
        reply = input(f"Is my guess {guess} too high(H) or too low(L) or correct(C)? :").lower()
        if reply == 'h':
            high=guess-1
        elif reply == 'l':
            low=guess+1
    print('Omg, I(Python) guessed it correctly dawg!')

computer_guess(55)




