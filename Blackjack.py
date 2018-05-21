#Jack Robey
#5/21/18
#Blackjack.py

amountP1 = 5000

wager = int(input('You have $5000. How much would you like to wager? The minimum is $2 and the maximum is $500. '))

if wager < 2:
    while True:
        print()
        wager = int(input('That wager does not meet with the restrictions ($2 is the minimum, $500 is the maximum). Enter another wager. '))
        if wager >= 2 and wager <= 500:
            break
if wager > 500:
    while True:
        print()
        wager = int(input('That wager does not meet with the restrictions ($2 is the minimum, $500 is the maximum). Enter another wager. '))
        if wager <= 500 and wager >= 2:
            break
if wager >= 2 and wager <= 500:
    

