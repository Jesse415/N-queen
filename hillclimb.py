import numpy as np
import math
import copy
import time

def hillclimb(initialBoard, n):
    listOfNeighbors = []
    fitnessScore = []
    h = 9999

    #-------------------
    # Generate Neighbors
    #-------------------
    for i in range(n):
        for j in range(n):
            newNeighbor = copy.deepcopy(initialBoard)
            if newNeighbor[i] != j:
                newNeighbor[i] = j
                listOfNeighbors.append(newNeighbor)

        #---------------------------------
        # Get the fitness of all neighbors
        #---------------------------------
    for i in range(len(listOfNeighbors)):
        fitnessScore.append(fitness(listOfNeighbors[i]))

        #--------------------------------
        # Get the board with best fitness
        #--------------------------------
    for i in range(len(fitnessScore)):
        if fitnessScore[i] < h:
            h = fitnessScore[i]
            initialBoard = listOfNeighbors[i]
    fitnessScore = []

    return (initialBoard, h)

#----------------
# Checking the H
# value Function
#---------------
def fitness(state):
    fitnessScore = 0
    for i in range(len(state)-1):
        for j in range(i+1, len(state)):

            #---------------------------------------
            # Checking for queens in the same column
            #---------------------------------------
            if state[i] == state[j]:
                fitnessScore += 1

            #----------------------
            # Checking for dia left
            #----------------------
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

        #--------------
        # Hill Climbing
        #--------------
        bestBoard, h = hillclimb(initialBoard, n)

        #----------------------------
        # If n=1 break and printBoard
        # elif n = 2 or 3 make h=0
        # for no solutions
        #----------------------------
        if n == 1:
            bestBoard = initialBoard
            break
        elif n == 2 or n == 3:
            h = 0


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
