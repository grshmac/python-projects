import random

words = [
    "apple", "banana", "grape", "orange", "mango", "peach", "melon", "cherry", "berry", "lemon",
    "table", "chair", "pillow", "sofa", "lamp", "blanket", "mirror", "shelf", "drawer", "carpet",
    "tiger", "lion", "zebra", "giraffe", "elephant", "panda", "monkey", "rabbit", "fox", "wolf",
    "pencil", "eraser", "notebook", "marker", "paper", "ruler", "scissors", "glue", "pen", "sharpener",
    "cloud", "rain", "snow", "storm", "wind", "sunny", "thunder", "foggy", "breeze", "lightning",
    "school", "garden", "friend", "family", "party", "holiday", "beach", "movie", "travel", "music",
    "pizza", "burger", "cookie", "cheese", "pasta", "bread", "noodle", "soup", "salad", "steak",
    "happy", "funny", "sleepy", "crazy", "brave", "smart", "kind", "silly", "lucky", "shy",
    "robot", "rocket", "space", "planet", "alien", "moon", "star", "galaxy", "comet", "astronaut",
    "magic", "witch", "ghost", "dragon", "castle", "sword", "forest", "pirate", "treasure", "island"
]

hangman= {0:('     ',
              '     ',
              '     '),
           1:('  o  ',
              '     ',
              '     '),
           2:('  o  ',
              '  |  ',
              '     '),
           3:('  o  ',
              ' /|  ',
              '     '),
           4:('  o  ',
              ' /|\\ ',
              '     '),
           5:('  o  ',
              ' /|\\ ',
              ' /   '),
           6:('  o  ',
              ' /|\\ ',
              ' / \\ ')}

word=random.choice(words).lower()
tries=0
guessed=set()
hint=['_' for letter in word]

while tries<=len(hangman)-1 and '_' in hint:
    print("Save Our Hangman!!!")
    for i in hangman[tries]:
        print(i)
    print("********************")

    print("".join(hint))

    guess = input("\nGuess a letter one at a time: ").lower()
    if len(guess)!=1 or not guess.isalpha():
        print("waitt, only one at a time and only alphanumeric.")
    if guess in guessed:
        print("you already guessed that letter")

    guessed.add(guess)
    if guess in word:
        for i,letter in enumerate(word):
            if letter==guess:
                hint[i]=guess
    else:
        tries+=1
        print(f"careful! you used {tries} tries out of 7\n")

if '_' not in hint:
    print("********************")
    print("\nyay you wonn")
    print(f'The word was {word}')

else:
    print("********************")
    print("\nyou lost, try again next time love:)")
    print(f'The word was {word}')



