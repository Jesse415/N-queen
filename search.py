import numpy as np
import math
import copy
import time
import collections


#TODO: Choose search method: Breadth-first, Hill climbing, or Simulated anneling search
#------------------------
# Breadth-first Search
# function
#------------------------
def bfs(board, n):
    #-----------------------
    # Deque meant to act as
    # a queue - FIFO
    #-----------------------
    movesMade = collections.deque()
    updateBoard = []

    #TODO: Do Breadth-first Search: if n=1-6 print number of solutions &
    # and visual graph, Else if n=7-20 only print number of solutions

    #------------------------------
    # for loop to place Queen in
    # every spot in i=0 and add
    # to deque/queue movesMade
    #------------------------------

    i = 0
    for j in range(len(board[i])):
        if board[i][j] == '-':
            board[i][j] = 'Q'
            movesMade.append(copy.deepcopy(board))
            board[i][j] = '-'

    #--------------------------------------------
    # While loop to pop deque/queue and
    # update the board with new placement
    # of queen in the following i then
    # adding it back to deque/queue. Effectively
    # making a breadth first search tree
    #--------------------------------------------
    while i < n-1:
        k=0
        i+=1
        while k < pow(n, i+1):
            updateBoard = movesMade.popleft()
            for j in range(len(updateBoard[i])):
                if updateBoard[i][j] == '-':
                    updateBoard[i][j] = 'Q'
                    movesMade.append(copy.deepcopy(updateBoard))
                    updateBoard[i][j] = '-'
                else:
                    break
                k+=1

    return movesMade

#-----------------------
# Hill-climbing Search
# function
#-----------------------
def hcs(grid):
    #TODO: Do Hill-climbing Search: If n<=8 print visual Else print
    # Number of solutions
    return something

#----------------------
# Simulated-anneling
# Search
#----------------------
def sa(grid):
    #TODO: Simulated-anneling Search: If n<=8 print visual Else print
    # Number of solutions
    return something

#-----------------------------------
# Function to determine the distance
# to solution
#-----------------------------------
def cost():
#TODO: Cost function determining the distance to solutions

    return distance

def vetForSolution(checkBoard, n):

    if n == 1:
        return True

    else:
        for y in range(len(checkBoard)):
            for x in range(len(checkBoard[y])):
                if checkBoard[y][x]=='Q': #Found a queen

                    #----------------------
                    # Check for column down
                    #----------------------
                    for j in range(y+1,n):
    	                if checkBoard[j][x] == 'Q':
      	                    return False

                    #--------------------------
                    # Check Diagonal Left Down
                    #--------------------------
                    for a,b in zip(range(x-1,-1,-1),range(y+1,n,1)):
    	                if checkBoard[b][a] == 'Q':
      	                    return False

                    #-----------------------------
                    # Check Diagonal Right Down
                    #-----------------------------
                    for a,b in zip(range(x+1,n),range(y+1,n,1)):
    	                if checkBoard[b][a] == 'Q':
      	                    return False

        return True

#------------------------
# Main Function asking
# for the initial input
#------------------------
def main():

    board = []
    solutions = []

    #-----------------------
    # Made to test different
    # inputs from user
    #-----------------------
    print("Please enter number for grid")
    n = int(input())

    #-----------------------
    # Builds the board needed
    # based on n
    #-----------------------
    board = np.full((n,n), '-')

    #-----------------------
    # Start time to solution
    #-----------------------
    start = time.time()
    time.process_time()

    #-------------------------
    # Part A: Do breadth first
    # search add it to tree
    #-------------------------
    movesMade = bfs(board, n)

    for x in range(len(movesMade)):
        possibleSolution = movesMade.popleft()

        if vetForSolution(possibleSolution, n) is True:
            solutions.append(copy.deepcopy(possibleSolution))

    #----------------------------
    # Print every branch of tree
    #----------------------------

    if solutions == 0:
        print("There are NO solutions")
    else:
        for i in range(len(solutions)):
            for j in range(len(solutions[i])):
                print("This j: ", j, solutions[i][j], end = " ")
                print()
            print()
        print("Number for Solutions: ", i+1)


    #-----------------------------
    # Time that taken to solution
    #-----------------------------
    elapsed = time.time() - start
    math.ceil(elapsed)
    print("Time from start to solution: ", round(elapsed, 1))

if __name__ == "__main__":
    main()
