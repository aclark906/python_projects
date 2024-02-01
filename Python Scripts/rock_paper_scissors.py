import random

options = ['rock', 'paper', 'scissors']
player1 = random.choice(options)
player2 = random.choice(options)


def rpsWinner(player1, player2):
    if player1 == player2:
        return 'tie'
    elif player1 == 'rock':
        if player2 == 'paper':
            return 'player two'
        elif player2 == 'scissors':
            return 'player one'
    elif player1 == 'paper':
        if player2 == 'rock':
            return 'player one'
        elif player2 == 'scissors':
            return 'player two'
    elif player1 == 'scissors':
        if player2 == 'rock':
            return 'player two'
        elif player2 == 'paper':
            return 'player one'


assert rpsWinner('rock', 'paper') == 'player two'

assert rpsWinner('rock', 'scissors') == 'player one'

assert rpsWinner('paper', 'scissors') == 'player two'

assert rpsWinner('paper', 'rock') == 'player one'

assert rpsWinner('scissors', 'rock') == 'player two'

assert rpsWinner('scissors', 'paper') == 'player one'

assert rpsWinner('rock', 'rock') == 'tie'

assert rpsWinner('paper', 'paper') == 'tie'

assert rpsWinner('scissors', 'scissors') == 'tie'    