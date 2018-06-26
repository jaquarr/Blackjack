#Jack Robey
#5/21/18
#Blackjack.py
from random import randint
from random import shuffle

amountU = 5000 #starting amount of cash for user

wager = int(input('You have $5000. How much would you like to wager? The minimum is $2 and the maximum is $500. ')) #prompts the user to wager
print()

if wager < 2: #stops the game if wager is less than $2
    while True:
        wager = int(input('That wager does not meet with the restrictions ($2 is the minimum, $500 is the maximum). Enter another wager. '))
        print()
        if wager >= 2 and wager <= 500:
            break

if wager > 500: #stops the game if wager is more than $500
    while True:
        wager = int(input('That wager does not meet the restrictions ($2 is the minimum, $500 is the maximum). Enter another wager. '))
        print()
        if wager <= 500 and wager >= 2:
            break

if wager >= 2 and wager <= 500: #case for when the wager is legal
    deck = [] #shuffles a deck of 52 cards
    for i in range(1,53):
        deck.append(i)
        shuffle(deck)

    scoreU = 0 #allows the score to be tallied
    scoreD = 0

    for i in range(0,3,2):
        if deck[i] == 1 or deck[i] == 2 or deck[i] == 3 or deck[i] == 4: #if cases for 
            print('You drew an ace!')
            print()
            ace = int(input('Would you like the ace to be worth 1 or 11 points?'))
            print()
            if ace == 1:
                scoreU = scoreU + 1
            if ace == 11:
                scoreU = scoreU + 11
            if ace > 1 and ace < 11:
                print('Error, an ace can ONLY be worth 1 or 11 points.')
                print()
        elif deck[i] == 5 or deck[i] == 6 or deck[i] == 7 or deck[i] == 8:
            print('You drew a 2!')
            print()
            scoreU = scoreU + 2
        elif deck[i] == 9 or deck[i] == 10 or deck[i] == 11 or deck[i] == 12:
            print('You drew a 3!')
            print()
            scoreU = scoreU + 3
        elif deck[i] == 13 or deck[i] == 14 or deck[i] == 15 or deck[i] == 16:
            print('You drew a 4!')
            print()
            scoreU = scoreU + 4
        elif deck[i] == 17 or deck[i] == 18 or deck[i] == 19 or deck[i] == 20:
            print('You drew a 5!')
            print()
            scoreU = scoreU + 5
        elif deck[i] == 21 or deck[i] == 22 or deck[i] == 23 or deck[i] == 24:
            print('You drew a 6!')
            print()
            scoreU = scoreU + 6
        elif deck[i] == 25 or deck[i] == 26 or deck[i] == 27 or deck[i] == 28:
            print('You drew a 7!')
            print()
            scoreU = scoreU + 7
        elif deck[i] == 29 or deck[i] == 30 or deck[i] == 31 or deck[i] == 32:
            print('You drew an 8!')
            print()
            scoreU = scoreU + 8
        elif deck[i] == 33 or deck[i] == 34 or deck[i] == 35 or deck[i] == 36:
            print('You drew a 9!')
            print()
            scoreU = scoreU + 9
        elif deck[i] == 37 or deck[i] == 38 or deck[i] == 39 or deck[i] == 40:
            print('You drew a 10!')
            print()
            scoreU = scoreU + 10
        elif deck[i] == 41 or deck[i] == 42 or deck[i] == 43 or deck[i] == 44:
            print('You drew a queen!')
            print()
            scoreU = scoreU + 10
        elif deck[i] == 45 or deck[i] == 46 or deck[i] == 47 or deck[i] == 48:
            print('You drew a king!')
            print()
            scoreU = scoreU + 10
        elif deck[i] == 49 or deck[i] == 50 or deck[i] == 51 or deck[i] == 52:
            print('You drew a jack!')
            print()
            scoreU = scoreU + 10

    for i in range(1,4,2):
        if deck[i] == 1 or deck[i] == 2 or deck[i] == 3 or deck[i] == 4: #if cases for 
            print('The dealer drew an ace!')
            print()
            if scoreD + 11 >= 17:
                ace = 11
                scoreD = scoreD + 11
            if scoreD + 11 < 17:
                x = randint(1,2)
                if x == 1:
                    ace = 1
                    scoreD = scoreD + 1
                if x == 2:
                    ace = 11
                    scoreD = scoreD + 11
        elif deck[i] == 5 or deck[i] == 6 or deck[i] == 7 or deck[i] == 8:
            print('The dealer drew a 2!')
            print()
            scoreD = scoreD + 2
        elif deck[i] == 9 or deck[i] == 10 or deck[i] == 11 or deck[i] == 12:
            print('The dealer drew a 3!')
            print()
            scoreD = scoreD + 3
        elif deck[i] == 13 or deck[i] == 14 or deck[i] == 15 or deck[i] == 16:
            print('The dealer drew a 4!')
            print()
            scoreD = scoreD + 4
        elif deck[i] == 17 or deck[i] == 18 or deck[i] == 19 or deck[i] == 20:
            print('The dealer drew a 5!')
            print()
            scoreD = scoreD + 5
        elif deck[i] == 21 or deck[i] == 22 or deck[i] == 23 or deck[i] == 24:
            print('The dealer drew a 6!')
            print()
            scoreD = scoreD + 6
        elif deck[i] == 25 or deck[i] == 26 or deck[i] == 27 or deck[i] == 28:
            print('The dealer drew a 7!')
            print()
            scoreD = scoreD + 7
        elif deck[i] == 29 or deck[i] == 30 or deck[i] == 31 or deck[i] == 32:
            print('The dealer drew an 8!')
            print()
            scoreD = scoreD + 8
        elif deck[i] == 33 or deck[i] == 34 or deck[i] == 35 or deck[i] == 36:
            print('The dealer drew a 9!')
            print()
            scoreD = scoreD + 9
        elif deck[i] == 37 or deck[i] == 38 or deck[i] == 39 or deck[i] == 40:
            print('The dealer drew a 10!')
            print()
            scoreD = scoreD + 10
        elif deck[i] == 41 or deck[i] == 42 or deck[i] == 43 or deck[i] == 44:
            print('The dealer drew a queen!')
            print()
            scoreD = scoreD + 10
        elif deck[i] == 45 or deck[i] == 46 or deck[i] == 47 or deck[i] == 48:
            print('The dealer drew a king!')
            print()
            scoreD = scoreD + 10
        elif deck[i] == 49 or deck[i] == 50 or deck[i] == 51 or deck[i] == 52:
            print('The dealer drew a jack!')
            print()
            scoreD = scoreD + 10

    print('Your score is',scoreU,'.')
    print()
    print("The dealer's score is",scoreD,'.')
    print()
    print(deck)
