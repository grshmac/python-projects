import random

words = ["starry","beautiful","pineapple","bangtan"]

def main():
    random_word = random.choice(words)
    hint=['_']*len(random_word)
    wrong_guesses = 0
    guessed_word = set()
    is_running = True

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)

        user_guess=input("Guess a letter: ").lower()
        if len(user_guess) != 1 or not user_guess.isalpha():
            print("please enter a single letter.")
            continue
        if user_guess in guessed_word:
            print("nah, you already guessed that letter.")
            continue

        guessed_word.add(user_guess)
        if user_guess in random_word:
            for i in range(len(random_word)):
                if random_word[i] == user_guess:
                    hint[i] = user_guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_hangman(wrong_guesses)
            correct_word(random_word)
            print("you guessed the word!")
            is_running = False
        elif wrong_guesses >= len(hangman)-1:
            display_hangman(wrong_guesses)
            correct_word(random_word)
            print("sorry, you did not guess the word!")
            is_running = False


def display_hangman(wrong_guesses):
    for i in hangman[wrong_guesses]:
        print(i)


def display_hint(hint):
    print("".join(hint))


def correct_word(random_word):
    print(" ".join(random_word))


#dictionary for art of hangman
hangman = {0:('     ',
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

if __name__ == '__main__':
    main()

