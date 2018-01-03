import matplotlib.pyplot as plt
import random

overall = 1000
profitPile = 0

dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]

diceRollDistribution = [0] * 12

progress = []

dontPassBet = 0
sixBet = 0
eightBet = 0
fiveBet = 0
nineBet = 0

pointEstablished = False
pointPlace = 0

wallet = 100
for b in range(0, 10):
    for i in range(0,1000):
        if wallet <= 0:
            break
        progress.append(wallet)
    
        if pointEstablished == False and dontPassBet == 0:
            wallet -= 10
            dontPassBet = 10
    
        diceValue = dice1[random.randint(0,5)] + dice2[random.randint(0,5)]
        #print diceValue
    
    
        if pointEstablished == False:
            if diceValue == 7 or diceValue == 11:
                dontPassBet = 0
    
            elif diceValue == 2 or diceValue == 3:
                wallet += 10
    
            elif (diceValue >= 4 and diceValue <= 6) or (diceValue >= 8 and diceValue <= 10):           
                
                pointPlace = diceValue
                pointEstablished = True
                
                """
                if dontPassBet != 10:
                    wallet -= 5
                    dontPassBet = 10
                """
                """
                if fiveBet == 0:
                    fiveBet = 5
                    wallet -= 5
                """  
                if sixBet == 0:
                    sixBet = 6
                    wallet -= 6
    
                if eightBet == 0:
                    eightBet = 6
                    wallet -= 6
                
                """
                if nineBet == 0:
                    nineBet = 5
                    wallet -= 5
                """
        else:
            if diceValue == 6 or diceValue == 8:
                wallet += 7
                """
                elif diceValue == 5 or diceValue == 9:
                    wallet += 6
                """
            elif diceValue == 7:
                wallet += 10
    
                #fiveBet = 0
    
                sixBet = 0
                eightBet = 0
    
                #nineBet = 0
    
                pointEstablished = False
                pointPlace = 0
            
            if diceValue == pointPlace:
    
                pointEstablished = False
                pointPlace = 0
    
                dontPassBet = 0

    overall += wallet - 100
    wallet = 100

print overall

#plt.figure(1)
#plt.plot(range(0, len(progress)), progress)


#plt.show()


