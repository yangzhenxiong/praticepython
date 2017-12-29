# coding=utf-8
'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to
the winner, and ask if the players want to start a new game)

Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock
'''
while True:
    print('This is a Rock-Paper-Scissors game')
    player1 = input('Player1, Please input your choice:')
    player2 = input('Player2, Please input your choice:')

    if('Rock' == player1 and 'Scissors' == player2):
        print("Player1 is the winner")
        break
    if('Rock' == player1 and 'Paper' == player2):
        print("Player2 is the winner")
        break
    if('Rock' == player1 and 'Rock' == player2):
        print("Once again!")
    if ('Scissors'== player1 and 'Rock' == player2):
        print("Player2 is the winner")
        break
    if ('Scissors' == player1 and 'Paper' == player2):
        print("Player1 is the winner")
        break
    if ('Scissors' == player1 and 'Scissors' == player2):
        print("Once again!")
    if ('Paper' == player1 and 'Rock' == player2):
        print("Player1 is the winner")
        break
    if ('Paper' == player1 and 'Paper' == player2):
        print("Once again!")
        break
    if ('Paper' == player1 and 'Scissors' == player2):
        print("Player2 is the winner")