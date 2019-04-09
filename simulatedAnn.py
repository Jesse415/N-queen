import numpy as np
import math
import copy
import time

def SA(initialBoard, n):
    e = 2.71828
    temp = 999
    coolingRate = 0.003

    #---------------------------------
    # Get the fitness for initialBoard
    #---------------------------------
    fitnessScore = fitness(initialBoard)
    newBoard = copy.deepcopy(initialBoard)

    while temp > 1:
        #-------------------------------
        # Pick a random Queen's position
        #-------------------------------
        ranQueen = np.random.randint(low=0, high=n)
        current = initialBoard[ranQueen]
        newPosition = current

        #-----------------------------------
        # Pick a random position to move the
        # Queen to
        #-----------------------------------
        while newPosition == current:
            newPosition = np.random.randint(low=0, high=n)

        newBoard[ranQueen] = newPosition

        #--------------
        # Check Fitness
        #--------------
        newFitScore = fitness(newBoard)

        r = np.random.uniform(0,1)
        p = e**-(newFitScore - fitnessScore)/temp

        #----------------------------
        # Move Queen to newPosition
        # or based of the probability
        # make the move
        #----------------------------
        if fitnessScore >= newFitScore:
            initialBoard = copy.deepcopy(newBoard)
            fitnessScore = newFitScore
        elif p < r:
            initialBoard = copy.deepcopy(newBoard)
            fitnessScore = newFitScore

        temp *= 1-coolingRate

    return (initialBoard, newFitScore)

def fitness(state):
    fitnessScore = 0
    for i in range(len(state)-1):
        for j in range(i+1, len(state)):

            #--------------------------------------
            #checking for queens in the same column
            #--------------------------------------
            if state[i] == state[j]:
                fitnessScore += 1
            #---------------------
            #checking for dia left
            #---------------------
            if state[i]-(j-i) == state[j]:
                fitnessScore += 1
            #--------------------
            # Check for dia right
            #--------------------
            if state[i]+(j-i) == state[j]:
                fitnessScore +=1
    return fitnessScore

#---------------------
# Print Board Function
#---------------------
def printBoard(finishedBoard):
    for i in range(len(finishedBoard)):
        for j in range(len(finishedBoard)):
            if j != finishedBoard[i]:
                print("-", end = " ")
            else:
                print("Q", end = " ")
        print()

def main():

    n = int(input("Please enter number for grid: "))
    h = 9999

    #-----------------------
    # Start time to solution
    #-----------------------
    start = time.time()
    time.process_time()

    while h > 0:
        #----------------------
        #random board generator
        #----------------------
        initialBoard = list(np.random.randint(low=0, high=n, size=n))

        #----------------------------
        # If n=1 break and printBoard
        # elif n = 2 or 3 make h=0
        # for no solutions
        #----------------------------
        if n == 1:
            bestBoard = initialBoard
            h = 0
            break
        elif n == 2 or n == 3:
            h = 0
            break

        #--------------------
        # Simmulated Anneling
        #--------------------
        bestBoard, h = SA(initialBoard, n)

    if n == 2 or n == 3:
        print("There are NO solutions.")
    else:
        printBoard(bestBoard)

    #-----------------------------
    # Time that taken to solution
    #-----------------------------
    elapsed = time.time() - start
    minutes = int(elapsed//60)
    hours = int(elapsed // 3600)
    #math.ceil(elapsed)
    print("Time: H:", hours,"M:",minutes,"S:",(round(elapsed, 4))%60)

main()
