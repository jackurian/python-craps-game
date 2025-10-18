import random
import crapshelp as ch
cont = True
balance = 100

helpy = input('Welcome to the Craps table? Would you like some help before you start? (y/n) ')
if (helpy == 'y'):
    help(ch.chart)
    ch.chart()
else:
    print('Alright, good luck! \n')

while (cont == True):
    bet = 0
    pbamount = 0
    print(f"You have ${balance} to spend.")
    bet = int(input("How much would you like to bet? "))
    print(f"You have placed a ${bet} bet.")
    balance = balance - bet

    earning = 0

    point = 0
    Result = 'C'

    pbdec = ''
    pbResult = 'C'
    pbplace = 0
    pbwinningnum = 0

    round = 1
    roundcount = 0

    while (Result != 'W' and Result != 'L'):

        dice1roll = random.randint(1,6)
        dice2roll = random.randint(1,6)

        roll = dice1roll + dice2roll

        print(f"\nThe shooter rolled a {dice1roll} and a {dice2roll}.")
        print(f"In total, he rolled a {roll}.")

        if (round == 1):
            if (roll == 2 or roll == 3 or roll == 12):
                print("You lose!")
                Result = 'L'
            elif (roll == 7 or roll == 11):
                print("You win!")
                Result = 'W'
                payoff = bet
            else:
                point = roll
                print(f"{point} is the new point. Roll a {point} before a 7 to win.")
                pbdec = input("Type 'c' to continue, or 'pb' to make a place bet. ")
                if (pbdec == 'pb'):
                    pbamount = int(input("How much would you like to bet? "))
                    pbplace = int(input("Which number will you place on? "))
                    balance = balance - pbamount
                else:
                    pbamount = 0
                    pbplace = 0     
        else:
            if (pbdec == 'pb' and roll == pbplace):
                if (pbwinningnum == 0):
                    print(f"It's a {roll}! You won your place bet! Collect your earnings.")
                else:
                    print("You already won the place bet.")
                pbResult = 'W'
                pbwinningnum = roll

            if (roll == 7):
                print("It's a 7! You lose!")
                Result = 'L'
                if (pbwinningnum == 0):
                    pbResult = 'L'
            elif (roll == point):
                print(f"It's a {roll}! He hit the point! You win!")
                Result = 'W'
            else:
                print(f"It's a {roll}.")
                input("Type 'c' to continue. ")

        round += 1
        roundcount += 1

    pbamount = float(pbamount)
    if (pbResult == 'W'):
        if (pbwinningnum == 4 or pbwinningnum == 10):
            pbpayoff = 1.8
        elif (pbwinningnum == 5 or pbwinningnum == 9):
            pbpayoff = 1.5
        elif (pbwinningnum == 6 or pbwinningnum == 8):
            pbpayoff = 1.167
        else:
            pbpayoff = 0
    elif (pbResult == 'L'):
        pbpayoff = 0
    else:
        pbpayoff = 1
    
    bet = float(bet)
    if (Result == 'W'):
            payoff = 0
            if (roll == 4 or roll == 10):
                payoff = 2
            elif (roll == 5 or roll == 9):
                payoff = 1.5
            elif (roll == 6 or roll == 8):
                payoff = 1.2
            else:
                payoff = 1
    if (Result == 'L'):
        payoff = 0

    earning = int(bet * payoff)
    pbearning = int(pbamount * pbpayoff)

    print(f"\nYou bet ${int(bet)} and came out with ${earning}, gaining you ${earning - int(bet)}.")
    if(pbdec == 'pb'):
        print(f"Additionally, your ${int(pbamount)} place bet on {pbplace} earned back ${pbearning}.")
    print(f"In total, your bets of ${int(bet) + int(pbamount)} yieled ${earning + pbearning}.")
    print(f"That round lasted {roundcount} rolls.")

    balance = balance + earning + pbearning

    if (balance <= 0):
        print("You're out of money! We're kicking you out.")
        cont = False
        break
    else:
        print(f"You have ${balance} left.")

    con = input("Play again? (y/n) ")
    if (con == 'y'):
        cont = True
    else:
        cont = False