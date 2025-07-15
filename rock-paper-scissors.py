import random

def rps():
    user=input('Enter between rock(r), paper(p) and scissors(s): ')

    computer_chooses=random.choice(['r', 'p', 's'])

    if user==computer_chooses:
        # print('That\'s a draw right there!')
        return 'That\'s a draw right there!'

    # elif (user=='p' and computer_chooses=='r') or (user=='s' and computer_chooses=='p') or (user=='r' and computer_chooses=='s'):
    #     print('User wins!')
        # return 'User wins!'

    elif is_win(user, computer_chooses):
        return 'User wins!'

    else:
        return 'Python wins!'
        # print('Python wins!')

#or create a separate func for winning case like
def is_win(player, opponent):
    if (player=='p' and opponent=='r') or (player=='s' and opponent=='p') or (player=='r' and opponent=='s'):
        return True

print(rps())