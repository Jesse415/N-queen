import numpy as np
import math
import copy
import time

def hillclimb(initialBoard, n):
    listOfNeighbors = []
    fitnessScore = []
    h = 9999

        # Generate Neighbors
    for i in range(n):
        for j in range(n):
            newNeighbor = copy.deepcopy(initialBoard)
            if newNeighbor[i] != j:
                newNeighbor[i] = j
                listOfNeighbors.append(newNeighbor)

        # Get the fitness of all neighbors
    for i in range(len(listOfNeighbors)):
        fitnessScore.append(fitness(listOfNeighbors[i]))

        # Get the board with best fitness
    for i in range(len(fitnessScore)):
        if fitnessScore[i] < h:
            h = fitnessScore[i]
            initialBoard = listOfNeighbors[i]
    fitnessScore = []

#    for i in range(len(listOfNeighbors)):
#        print(listOfNeighbors[i])

    return (initialBoard, h)

def fitness(state):
    fitnessScore = 0
    for i in range(len(state)-1):
        for j in range(i+1, len(state)):
            #checking for queens in the same column
            if state[i] == state[j]:
                fitnessScore += 1
            #checking for dia left
            if state[i]-(j-i) == state[j]:
                fitnessScore += 1
            # Check for dia right
            if state[i]+(j-i) == state[j]:
                fitnessScore +=1
    return fitnessScore

def printBoard(finishedBoard):
    for i in range(len(finishedBoard)):
        for j in range(len(finishedBoard)):
            if j != finishedBoard[i]:
                print("-", end = " ")
            else:
                print("Q", end = " ")
        print()

def main():

    #n = int(input("Get n: "))
    n = 7
    h = 9999

    while h > 0:
        #random board generator
        initialBoard = list(np.random.randint(low=0, high=n, size=n))

        # Hill Climbing
        bestBoard, h = hillclimb(initialBoard, n)

    printBoard(bestBoard)

main()