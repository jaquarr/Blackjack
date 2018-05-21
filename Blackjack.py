#Jack Robey
#5/21/18
#Blackjack.py

amountP1 = 5000

wager = int(input('You have $5000. How much would you like to wager? The minimum is $2 and the maximum is $500. '))

while True:
    if wager < 2:
        print()
        wager = int(input('That wager is too low. The wager must at least be $2, so enter a different wager. '))
        if wager > 2:
            break
    if wager > 500:
        print()
        wager = int(input('That wager is too high. The wager must at most be $500, so enter a different wager. '))
        if wager < 500:
            break


