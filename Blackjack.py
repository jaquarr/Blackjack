#Jack Robey
#5/21/18
#Blackjack.py
from random import randint

amountP1 = 5000 #starting amount of cash for user

wager = int(input('You have $5000. How much would you like to wager? The minimum is $2 and the maximum is $500. ')) #prompts the user to wager

if wager < 2: #stops the game if wager is less than $2
    while True:
        print()
        wager = int(input('That wager does not meet with the restrictions ($2 is the minimum, $500 is the maximum). Enter another wager. '))
        if wager >= 2 and wager <= 500:
            break
if wager > 500: #stops the game if wager is more than $500
    while True:
        print()
        wager = int(input('That wager does not meet the restrictions ($2 is the minimum, $500 is the maximum). Enter another wager. '))
        if wager <= 500 and wager >= 2:
            break
if wager >= 2 and wager <= 500: #case for when the wager is legal
    deck = [] #shuffles a deck of 52 cards
    for i in range(1,53):
        deck.append(0)
    for i in range(1,53):
        x = randint(0,51)
        if deck[x] == 0:
            deck[x] = i
        elif deck[x] != 0:
            for j in range(-1,51):
                j = j + 1
                if deck[j] == 0:
                    deck[j] = i
                    break
    card1P1 = deck[0]
    card2P1 = deck[1]
    scoreP1 = 0
    if deck[0] == 1 or deck[0] == 2 or deck[0] == 3 or deck[0] == 4:
        print('You drew an ace!')
        ace = int(input('Would you like the ace to be worth 1 or 11 points?'))
        if ace == 1:
            scoreP1 = scoreP1 + 1
        if ace == 11:
            scoreP1 = scoreP1 + 11
        if ace > 1 and ace < 11:
            print('Error, an ace can ONLY be worth 1 or 11 points.')
    elif deck[0] == 5 or deck[0] == 6 or deck[0] == 7 or deck[0] == 8:
        print('You drew a 2!')
        scoreP1 = scoreP1 + 2
    elif deck[0] == 9 or deck[0] == 10 or deck[0] == 11 or deck[0] == 12:
        print('You drew a 3!')
        scoreP1 = scoreP1 + 3
    elif deck[0] == 13 or deck[0] == 14 or deck[0] == 15 or deck[0] == 16:
        print('You drew a 4!')
        scoreP1 = scoreP1 + 4
    elif deck[0] == 17 or deck[0] == 18 or deck[0] == 19 or deck[0] == 20:
        print('You drew a 5!')
        scoreP1 = scoreP1 + 5
    elif deck[0] == 21 or deck[0] == 22 or deck[0] == 23 or deck[0] == 24:
        print('You drew a 6!')
        scoreP1 = scoreP1 + 6
    elif deck[0] == 25 or deck[0] == 26 or deck[0] == 27 or deck[0] == 28:
        print('You drew a 7!')
        scoreP1 = scoreP1 + 7
    elif deck[0] == 29 or deck[0] == 30 or deck[0] == 31 or deck[0] == 32:
        print('You drew a 8!')
        scoreP1 = scoreP1 + 8
    elif deck[0] == 33 or deck[0] == 34 or deck[0] == 35 or deck[0] == 36:
        print('You drew a 9!')
        scoreP1 = scoreP1 + 9
    elif deck[0] == 37 or deck[0] == 38 or deck[0] == 39 or deck[0] == 40:
        print('You drew a 10!')
        scoreP1 = scoreP1 + 10
    elif deck[0] == 41 or deck[0] == 42 or deck[0] == 43 or deck[0] == 44:
        print('You drew a queen!')
        scoreP1 = scoreP1 + 10
    elif deck[0] == 45 or deck[0] == 46 or deck[0] == 47 or deck[0] == 48:
        print('You drew a king!')
        scoreP1 = scoreP1 + 10
    elif deck[0] == 49 or deck[0] == 50 or deck[0] == 51 or deck[0] == 52:
        print('You drew a jack!')
        scoreP1 = scoreP1 + 10
    if deck[1] == 1 or deck[1] == 2 or deck[1] == 3 or deck[1] == 4:
        print('You drew an ace!')
        ace = int(input('Would you like the ace to be worth 1 or 11 points?'))
        if ace == 1:
            scoreP1 = scoreP1 + 1
        if ace == 11:
            scoreP1 = scoreP1 + 11
        if ace > 1 and ace < 11:
            print('Error, an ace can ONLY be worth 1 or 11 points.')
    elif deck[1] == 5 or deck[1] == 6 or deck[1] == 7 or deck[1] == 8:
        print('You drew a 2!')
        scoreP1 = scoreP1 + 2
    elif deck[1] == 9 or deck[1] == 10 or deck[1] == 11 or deck[1] == 12:
        print('You drew a 3!')
        scoreP1 = scoreP1 + 3
    elif deck[1] == 13 or deck[1] == 14 or deck[1] == 15 or deck[1] == 16:
        print('You drew a 4!')
        scoreP1 = scoreP1 + 4
    elif deck[1] == 17 or deck[1] == 18 or deck[1] == 19 or deck[1] == 20:
        print('You drew a 5!')
        scoreP1 = scoreP1 + 5
    elif deck[1] == 21 or deck[1] == 22 or deck[1] == 23 or deck[1] == 24:
        print('You drew a 6!')
        scoreP1 = scoreP1 + 6
    elif deck[1] == 25 or deck[1] == 26 or deck[1] == 27 or deck[1] == 28:
        print('You drew a 7!')
        scoreP1 = scoreP1 + 7
    elif deck[1] == 29 or deck[1] == 30 or deck[1] == 31 or deck[1] == 32:
        print('You drew a 8!')
        scoreP1 = scoreP1 + 8
    elif deck[1] == 33 or deck[1] == 34 or deck[1] == 35 or deck[1] == 36:
        print('You drew a 9!')
        scoreP1 = scoreP1 + 9
    elif deck[1] == 37 or deck[1] == 38 or deck[1] == 39 or deck[1] == 40:
        print('You drew a 10!')
        scoreP1 = scoreP1 + 10
    elif deck[1] == 41 or deck[1] == 42 or deck[1] == 43 or deck[1] == 44:
        print('You drew a queen!')
        scoreP1 = scoreP1 + 10
    elif deck[1] == 45 or deck[1] == 46 or deck[1] == 47 or deck[1] == 48:
        print('You drew a king!')
        scoreP1 = scoreP1 + 10
    elif deck[1] == 49 or deck[1] == 50 or deck[1] == 51 or deck[1] == 52:
        print('You drew a jack!')
        scoreP1 = scoreP1 + 10
    print(deck)
    print(scoreP1)

