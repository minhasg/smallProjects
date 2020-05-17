#!/usr/bin/python3
import random

PREDICT_HIGHER  = 0
PREDICT_LOWER   = 1
PREDICT_EQUAL   = 2

class HiLow():
    def __init__(self):
        self.prediction = None
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.sum = 0
        self.lose = False
    
    def printGame(self):
        print("Dice roll: {0} {1} {2} {3} | Sum: {4}".format(self.a, self.b, self.c, self.d, self.sum))
        # print("LOSE: {0}".format(self.lose))
        
    def play(self):
        self.a = random.randrange(1, 7) 
        self.b = random.randrange(1, 7)
        self.c = random.randrange(1, 7)
        self.d = random.randrange(1, 7)
        self.predictionCheck()
        self.sum = self.a + self.b + self.c + self.d
        self.printGame()
        return (not self.lose)
    
    def predict(self, prediction):
        self.prediction = prediction

    def predictionCheck(self):
        if self.prediction == None:
            self.lose = False
            return
        
        newSum = self.a + self.b + self.c + self.d
        if self.prediction == PREDICT_EQUAL:
            self.lose = newSum != self.sum
        
        elif self.prediction == PREDICT_HIGHER:
            self.lose = newSum <= self.sum
        
        elif self.prediction == PREDICT_LOWER:
            self.lose = newSum >= self.sum

def printProbabilities():
    probabilities = {}
    for w in range(1,7):
        for x in range(1,7):
            for y in range(1,7):
                for z in range(1,7):
                    s = w + x + y + z
                    if s not in probabilities.keys():
                        probabilities[s] = 0
                    probabilities[s] += 1

    totalCombinations = 6**4
    print("Probability of each roll:")
    for key in probabilities.keys():
        print("{0} | {1:.3}%".format(key, 100 * float(probabilities[key])/float(totalCombinations)))


if __name__ == "__main__":
    print("Welcome to high low dice!")
    print("In this game 4 die are rolled and the player must guess whether the next roll will be higher or lower than the current roll")
    print("Guess right 5 times in a row and you win!")
    print("Would you like to play? (y/n)")
    response = input(">>> ")
    print("")
    validResponses = ["y", "n", "p"]
    while not response in validResponses:
        response = input(">>> ")
        print("Response invalid, enter 'y' or 'n'")
        print("")
    
    if response == "n":
        print("Aww sad to see you go")
        exit()

    elif response == "p":
        printProbabilities()
        exit()

    print("Okay let's play") 
    print("")
    
    random.seed(None)
    play = True
    while play:
        hiLow = HiLow()
        lose = False
        index = 0
        validResponses = ["h", "l", "q", "e", "H", "L", "Q", "E"]
        while not lose:
            response = ""
            index += 1
            if index > 1: 
                print("[H]igher, [l]ower, or [e]qual? Or enter 'q' to quit")
                while not response in validResponses:
                    response = input(">>> ")
                    print("")
                
                if response == "h" or response == "H":
                    hiLow.predict(PREDICT_HIGHER)

                elif response == "l" or response == "L":
                    hiLow.predict(PREDICT_LOWER)
                
                elif response == "e" or response == "E":
                    hiLow.predict(PREDICT_EQUAL)

                else:
                    print("Goodbye")
                    exit()
            
            print("Round {0}".format(index))
            if not hiLow.play():
                lose = True
                    
            if index == 5:
                break

        if lose:
            print("Haha what a woob you lose")

        elif not lose:
            print("Congratulations you win!")

        print("Play again? (y/n)")
        response = input(">>> ")
        play = response == "y"
        print("")
