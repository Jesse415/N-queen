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
    count = 1

    #TODO: Do Breadth-first Search: if n=1-6 print number of solutions &
    # and visual graph, Else if n=7-20 only print number of solutions

    #------------------------------
    # for loop to place Queen in
    # every possible spot and add
    # to deque/queue power of n to count
    #------------------------------

    i = 0
    for j in range(len(board[i])):
        if board[i][j] == '-':
            board[i][j] = 'Q'
            movesMade.append(copy.deepcopy(board))
            board[i][j] = '-'

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

        #--------------Print deque--------
    i=0
    for i in range(len(movesMade)):
        print("I: ", i)
        for j in range(len(movesMade[i])):
            print("This j: ", j, movesMade[i][j], end = " ")
            print()
        print('\n')


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
# Function to determin the distance
# to solution
#-----------------------------------
def cost():
#TODO: Cost function determining the distance to solutions

    return distance


#------------------------
# Main Function asking
# for the initial input
#------------------------
#TODO: Hardcode n= 1-20

def main():

    board = []

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

    #----------------------------
    # Print every branch of tree
    #----------------------------
#    for i in range(len(movesMade)):
#        print("I: ", i)
#        for j in range(len(movesMade[i])):
#            print("This j: ", j, movesMade[i][j], end = " ")
#            print()
#        print('\n')

    #-----------------------------
    # Time that taken to solution
    #-----------------------------
    elapsed = time.time() - start
    math.ceil(elapsed)
    print("Time from start to solution: ", round(elapsed, 1))

if __name__ == "__main__":
    main()
