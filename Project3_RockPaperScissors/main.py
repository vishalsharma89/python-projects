# play with computer Rock , paper Scissors.
import random


def play():
    user = input(
        "What's your choice? \n'r' for rock, 'p' for paper,'s' fro scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It is a Tie!!"

    # r>s,s>p,p>r
    if is_win(user, computer):
        return 'You Won!', f'Computer chooses {computer}'

    # print(f"Computer chosses {opponent}")
    return 'You Lost!', f'Computer chooses {computer}'


def is_win(player, opponent):
    # return true if player wins
    # r>s,s>p,p>r
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())
