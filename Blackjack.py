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
            while True:
                if ace == 1:
                    scoreU = scoreU + 1
                    break
                if ace == 11:
                    scoreU = scoreU + 11
                    break
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

    if deck[1] == 1 or deck[1] == 2 or deck[1] == 3 or deck[1] == 4: #if cases for 
        print('The dealer drew an ace for his first card!')
        print()
        x = randint(1,2)
        if x == 1:
            ace = 1
            scoreD = scoreD + 1
        if x == 2:
            ace = 11
            scoreD = scoreD + 11
    elif deck[1] == 5 or deck[1] == 6 or deck[1] == 7 or deck[1] == 8:
        print('The dealer drew a 2 for his first card!')
        print()
        scoreD = scoreD + 2
    elif deck[1] == 9 or deck[1] == 10 or deck[1] == 11 or deck[1] == 12:
        print('The dealer drew a 3 for his first card!')
        print()
        scoreD = scoreD + 3
    elif deck[1] == 13 or deck[1] == 14 or deck[1] == 15 or deck[1] == 16:
        print('The dealer drew a 4 for his first card!')
        print()
        scoreD = scoreD + 4
    elif deck[1] == 17 or deck[1] == 18 or deck[1] == 19 or deck[1] == 20:
        print('The dealer drew a 5 for his first card!')
        print()
        scoreD = scoreD + 5
    elif deck[1] == 21 or deck[1] == 22 or deck[1] == 23 or deck[1] == 24:
        print('The dealer drew a 6 for his first card!')
        print()
        scoreD = scoreD + 6
    elif deck[1] == 25 or deck[1] == 26 or deck[1] == 27 or deck[1] == 28:
        print('The dealer drew a 7 for his first card!')
        print()
        scoreD = scoreD + 7
    elif deck[1] == 29 or deck[1] == 30 or deck[1] == 31 or deck[1] == 32:
        print('The dealer drew an 8 for his first card!')
        print()
        scoreD = scoreD + 8
    elif deck[1] == 33 or deck[1] == 34 or deck[1] == 35 or deck[1] == 36:
        print('The dealer drew a 9 for his first card!')
        print()
        scoreD = scoreD + 9
    elif deck[1] == 37 or deck[1] == 38 or deck[1] == 39 or deck[1] == 40:
        print('The dealer drew a 10 for his first card!')
        print()
        scoreD = scoreD + 10
    elif deck[1] == 41 or deck[1] == 42 or deck[1] == 43 or deck[1] == 44:
        print('The dealer drew a queen for his first card!')
        print()
        scoreD = scoreD + 10
    elif deck[1] == 45 or deck[1] == 46 or deck[1] == 47 or deck[1] == 48:
        print('The dealer drew a king for his first card!')
        print()
        scoreD = scoreD + 10
    elif deck[1] == 49 or deck[1] == 50 or deck[1] == 51 or deck[1] == 52:
        print('The dealer drew a jack for his first card!')
        print()
        scoreD = scoreD + 10

    print('Your score is',scoreU,'.')
    print()
    print("The dealer's score is",scoreD,'.')
    print()

    for x in range(4,52):
        choice = input('Hit or stand? Type "hit" to hit and "stand" to stand. ')
        print()
        if choice == 'hit':
            if deck[x] == 1 or deck[x] == 2 or deck[x] == 3 or deck[x] == 4: #if cases for 
                print('You drew an ace!')
                print()
                ace = int(input('Would you like the ace to be worth 1 or 11 points?'))
                print()
                while True:
                    if ace == 1:
                        scoreU = scoreU + 1
                        print('Your score is',scoreU,'.')
                        print()
                        break
                    if ace == 11:
                        scoreU = scoreU + 11
                        print('Your score is',scoreU,'.')
                        print()
                        break
            elif deck[x] == 5 or deck[x] == 6 or deck[x] == 7 or deck[x] == 8:
                print('You drew a 2!')
                print()
                scoreU = scoreU + 2
                print('Your score is',scoreU,'.')
                print()
            elif deck[x] == 9 or deck[x] == 10 or deck[x] == 11 or deck[x] == 12:
                print('You drew a 3!')
                print()
                scoreU = scoreU + 3
                print('Your score is',scoreU,'.')
                print()
            elif deck[x] == 13 or deck[x] == 14 or deck[x] == 15 or deck[x] == 16:
                print('You drew a 4!')
                print()
                scoreU = scoreU + 4
                print('Your score is',scoreU,'.')
                print()
            elif deck[x] == 17 or deck[x] == 18 or deck[x] == 19 or deck[x] == 20:
                print('You drew a 5!')
                print()
                scoreU = scoreU + 5
                print('Your score is',scoreU,'.')
                print()
            elif deck[x] == 21 or deck[x] == 22 or deck[x] == 23 or deck[x] == 24:
                print('You drew a 6!')
                print()
                scoreU = scoreU + 6
                print('Your score is',scoreU,'.')
                print()
            elif deck[x] == 25 or deck[x] == 26 or deck[x] == 27 or deck[x] == 28:
                print('You drew a 7!')
                print()
                scoreU = scoreU + 7
                print('Your score is',scoreU,'.')
                print()
            elif deck[x] == 29 or deck[x] == 30 or deck[x] == 31 or deck[x] == 32:
                print('You drew an 8!')
                print()
                scoreU = scoreU + 8
                print('Your score is',scoreU,'.')
                print()
            elif deck[x] == 33 or deck[x] == 34 or deck[x] == 35 or deck[x] == 36:
                print('You drew a 9!')
                print()
                scoreU = scoreU + 9
                print('Your score is',scoreU,'.')
                print()
            elif deck[x] == 37 or deck[x] == 38 or deck[x] == 39 or deck[x] == 40:
                print('You drew a 10!')
                print()
                scoreU = scoreU + 10
                print('Your score is',scoreU,'.')
                print()
            elif deck[x] == 41 or deck[x] == 42 or deck[x] == 43 or deck[x] == 44:
                print('You drew a queen!')
                print()
                scoreU = scoreU + 10
                print('Your score is',scoreU,'.')
                print()
            elif deck[x] == 45 or deck[x] == 46 or deck[x] == 47 or deck[x] == 48:
                print('You drew a king!')
                print()
                scoreU = scoreU + 10
                print('Your score is',scoreU,'.')
                print()
            elif deck[x] == 49 or deck[x] == 50 or deck[x] == 51 or deck[x] == 52:
                print('You drew a jack!')
                print()
                scoreU = scoreU + 10
                print('Your score is',scoreU,'.')
                print()
        if choice == 'stand':
                print('Your score is',scoreU,'.')
                break
    print(deck)