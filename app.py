from random import randint


def rockPaperScissors():
    yourHand = input('Tpye 1 for Rock, 2 for Paper, 3 for Scissors,'
                     'or leave empty for a random outcome: ')
    randomOptions = ['Rock', 'Paper', 'Scissors']
    enemyHand = randomOptions[randint(0, 2)]

    if yourHand == '1':
        yourHand = 'Rock'
    elif yourHand == '2':
        yourHand = 'Paper'
    elif yourHand == '3':
        yourHand = 'Scissors'
    elif yourHand == '':
        yourHand = ['Rock', 'Paper', 'Scissors']
        yourHand = yourHand[randint(0, 2)]

    def winLose():
        if yourHand == 'Rock' and enemyHand == 'Rock':
            return('tie')
        elif yourHand == 'Rock' and enemyHand == 'Paper':
            return('lose')
        elif yourHand == 'Rock' and enemyHand == 'Scissors':
            return('win')
        elif yourHand == 'Paper' and enemyHand == 'Rock':
            return('win')
        elif yourHand == 'Paper' and enemyHand == 'Paper':
            return('tie')
        elif yourHand == 'Paper' and enemyHand == 'Scissors':
            return('lose')
        elif yourHand == 'Scissors' and enemyHand == 'Rock':
            return('lose')
        elif yourHand == 'Scissors' and enemyHand == 'Paper':
            return('win')
        elif yourHand == 'Scissors' and enemyHand == 'Scissors':
            return('tie')

    print(f'You picked {yourHand}, your enemy chose {enemyHand}.'
          f' You {winLose()}.')


rockPaperScissors()
