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
    if deck[0] or deck[1] == 1 or 2 or 3 or 4:
        print('You drew an ace!')
        ace = int(input('Would you like the ace to be worth 1 or 11 points?'))
        if ace == 1:
            scoreP1 = scoreP1 + 1
        if ace == 11:
            scoreP1 = scoreP1 + 11
        if ace > 1 and ace < 11:
            print('Error, an ace can ONLY be worth 1 or 11 points.')
    if deck[0] or deck[1] == 5 or 6 or 7 or 8:
        print('You drew a 2!')
        scoreP1 = scoreP1 + 2
    if deck[0] or deck[1] == 9 or 10 or 11 or 12:
        print('You drew a 3!')
        scoreP1 = scoreP1 + 3
    if deck[0] or deck[1] == 13 or 14 or 15 or 16:
        print('You drew a 4!')
        scoreP1 = scoreP1 + 4
    if deck[0] or deck[1] == 17 or 18 or 19 or 20:
        print('You drew a 5!')
        scoreP1 = scoreP1 + 5
    if deck[0] or deck[1] == 21 or 22 or 23 or 24:
        print('You drew a 6!')
        scoreP1 = scoreP1 + 6
    if deck[0] or deck[1] == 25 or 26 or 27 or 28:
        print('You drew a 7!')
        scoreP1 = scoreP1 + 7
    if deck[0] or deck[1] == 29 or 30 or 31 or 32:
        print('You drew a 8!')
        scoreP1 = scoreP1 + 8
    if deck[0] or deck[1] == 33 or 34 or 35 or 36:
        print('You drew a 9!')
        scoreP1 = scoreP1 + 9
    if deck[0] or deck[1] == 37 or 38 or 39 or 40:
        print('You drew a 10!')
        scoreP1 = scoreP1 + 10
    if deck[0] or deck[1] == 41 or 42 or 43 or 44:
        print('You drew a queen!')
        scoreP1 = scoreP1 + 10
    if deck[0] or deck[1] == 45 or 46 or 47 or 48:
        print('You drew a king!')
        scoreP1 = scoreP1 + 10
    if deck[0] or deck[1] == 49 or 50 or 51 or 52:
        print('You drew a jack!')
        scoreP1 = scoreP1 + 10
    print(deck)

