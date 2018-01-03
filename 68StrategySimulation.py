import matplotlib.pyplot as plt
import random

dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]

losingTurns = [0] * 50



for j in range(0, 2000):

    progress = []
    
    pointEstablished = False
    pointPlace = 0
    
    sixBet = 0
    eightBet = 0
    
    wallet = 100

    for i in range(0, 1000):

        progress.append(wallet)
    
        if wallet <= 0:
            losingTurns[i / 20] += 1
            break
        
        diceSum = dice1[random.randint(0,5)] + dice2[random.randint(0,5)]
    
        if pointEstablished == False:
            if (diceSum >= 4 and diceSum <= 6) or (diceSum >= 8 and diceSum <= 10):
                pointEstablished = True
                pointPlace = diceSum
                
                if sixBet == 0 and eightBet == 0:
                    wallet -= 12
                    sixBet = 6
                    eightBet = 6
        else:
            if diceSum == 6:
                wallet += sixBet * (7/6)
                wallet -= 2
                sixBet += 2
            elif diceSum == 8:
                wallet += eightBet * (7/6)
                wallet -= 2
                eightBet += 2
            elif diceSum == 7:
                sixBet = 0
                eightBet = 0
                pointEstablished = False
                pointPlace = 0
    
            if diceSum == pointPlace:
                pointEstablished = False
                pointPlace = 0
            
    
    plt.figure(1)
    plt.plot(range(0, len(progress)), progress)

plt.title("6/8 strategy after 1000 rolls, ran 2000 times")
plt.xlabel("Number of rolls")
plt.ylabel("Money in account")

plt.figure(2)
li = range(0, len(losingTurns))
li[:] = [x * 20 for x in li]
plt.bar(li, losingTurns)

plt.title("Distribution of how many rolls it takes to lose bankroll")
plt.xlabel("Number of rolls")
plt.ylabel("Frequency of loss")

plt.show()


