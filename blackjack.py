# Alex Humphries
# 5/26/2021

# Blackjack

# Rules of blackjack
# Goal is 21
# Cardsssssssss
# Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King
# Ace is 1 or 11
# Each player starts with two cards
# you are given a card
# Hit or stand
# The goal of blackjack is to beat the
# dealer's hand without going over 21.
# Dealer will hit until his/her cards total 17 or higher


import random
def main():
    #cards
    deck = ['CA', 'C2', 'C3', 'C4','C5','C6','C7','C8','C9','C10',
            'CJ','CQ','CK','DA', 'DA','D2', 'D3', 'D4','D5','D6','D7','D8','D9','D10',
            'DJ','DQ','DK','HA', 'H2', 'H3', 'H4','H5','H6','H7','H8','H9','H10',
            'HJ','HQ','HK','SA', 'S2', 'S3', 'S4','S5','S6','S7','S8','S9','S10',
            'SJ','SQ','SK']
    print('Hello welcome to blackjack!')
    print('The dealer will now deal your hand!')
    print('Please note, the letter in front of your card is the suit,',
          'i.e. C stands for Clubs. The number after is the value of the card.')
    print('To start, the house will loan you $100.')
    playerTotal = 100.00
    print('')
    userChoice = input('Press D to deal, or E to exit: ')
    while userChoice == 'D':
        bet = float(input('Please enter how much you are betting, in 10 dollar increments. (Only type the numbers.)'))
        earnings = 0
        playerTotal -= bet
        print('')
        print('You have bet:', bet, 'your total is now:', playerTotal)
        userHand,userTotal = user(userChoice, deck)
        cpuHand, cpuTotal = cpu(deck)
        print('Your hand is',userHand)
        print('That makes your total',userTotal)
        print('')
        userIn = input('Press H to hit or S to stand: ')
        while userIn == 'H' or userIn == 'S':     
            if userIn == 'H' or userIn == 'h':
                userHand, userTotal, cpuHand, cpuTotal = hit(userHand,userTotal, cpuHand,cpuTotal,deck)
                print('Your hand is',userHand)
                print('That makes your total',userTotal)
                if(userTotal > 21):
                    print('You bust!')
                    break
                elif(userTotal <= 21):
                    userIn = input('Press H to hit or S to stand: ')
            elif userIn == 'S' or userIn == 's':
                print('The dealer has:', cpuHand, 'which has a total of', cpuTotal, 'versus your', userTotal)
                if userTotal <= 21:
                    if userTotal > cpuTotal:
                        print('You win!')
                        earnings = bet *2 
                        playerTotal += earnings
                        break
                    elif userTotal == cpuTotal:
                        print('It\'s a tie!')
                        playerTotal+= bet
                    elif cpuTotal <21 and cpuTotal > playerTotal:
                        print('Dealer wins!')
                        break
                    elif userTotal > 21:
                        print('Bust!')
                        break
                        
        print('')
        print('Your money total is now:', playerTotal)
        userChoice = input('Press D to deal again, or E to exit: ')
    print('Thank you for playing with us!')
    print('Total earnings:', earnings)
            
def user(userIn, deck):
    
    userHand = []
    if userIn =='D' or userIn == 'd':
        firstChoice = random.randint(0,len(deck))
        userHand.append(deck[firstChoice])
        del deck[firstChoice]
        secondChoice = random.randint(0,len(deck))
        userHand.append(deck[secondChoice])
        del deck[secondChoice]
        handTotal = 0
        for element in userHand:
            strNumber = str(element)
            for digit in strNumber:
                if digit == 'J' or digit =='Q' or digit == 'K' or digit.isdigit() and int(digit) == 1:
                    handTotal += 10
                elif digit =='A':
                    handTotal +=1
                elif digit.isdigit():
                    handTotal += int(digit)
    return userHand, handTotal

def cpu(deck):
    
    cpuHand = []
    firstChoice = random.randint(0,len(deck))
    cpuHand.append(deck[firstChoice])
    del deck[firstChoice]
    secondChoice = random.randint(0,len(deck))
    cpuHand.append(deck[secondChoice])
    del deck[secondChoice]
    cpuTotal = 0
    for element in cpuHand:
        strNumber = str(element)
        for digit in strNumber:
            if digit == 'J' or digit =='Q' or digit == 'K' or digit.isdigit() and int(digit) == 1:
                cpuTotal += 10
            elif digit =='A':
                cpuTotal +=1
            elif digit.isdigit():
                cpuTotal += int(digit)
    return cpuHand, cpuTotal
        
    

def hit(userHand, userTotal, cpuHand, cpuTotal, deck):
    ran1 = random.randint(0,len(deck))
    userHand.append(deck[ran1])
    del deck[ran1]
    ran2 = random.randint(0, len(deck))
    cpuHand.append(deck[ran2])
    del deck[ran2]
    strNumber = str(userHand[-1])
    for digit in strNumber:
        if digit == 'J' or digit =='Q' or digit == 'K' or digit.isdigit() and int(digit) == 1:
            userTotal += 10
        elif digit =='A':
            userTotal +=1
        elif digit.isdigit():
            userTotal += int(digit)
    strNumber2 = str(cpuHand[-1])
    for digit in strNumber2:
        if digit == 'J' or digit =='Q' or digit == 'K' or digit.isdigit() and int(digit) == 1:
            cpuTotal += 10
        elif digit =='A':
            cpuTotal +=1
        elif digit.isdigit():
            cpuTotal += int(digit)
    return userHand, userTotal, cpuHand, cpuTotal


main()
