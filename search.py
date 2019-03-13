import math
import copy
import time
import collections


#TODO: Choose search method: Breadth-first, Hill climbing, or Simulated anneling search
#------------------------
# Breadth-first Search
# function
#------------------------
def bfs(board):
    array = []
    movesMade = collections.deque()

    #TODO: Do Breadth-first Search: if n=1-6 print number of solutions &
    # and visual graph, Else if n=7-20 only print number of solutions
    for i in range(len(board)):
        print("This is i: ", i, board[i])
        print()
        for j in range(len(board[i])):
            if board[i][j] == 0:
                board[i][j] = 'Q'
                movesMade.append(copy.deepcopy(board))
                board[i][j] = 0
        print()

   # for i in range(len(movesMade)):
   #     for j in range(len(movesMade)):
   #         print("MovesMade Print: ", movesMade[i][j], end = " ")
   #     print()
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
    # This for loop builds
    # The board needed based
    # on n
    #-----------------------
    for i in range(n):
        array = [0] * n
        board.append(array)

    #-----------------------
    # Start time to solution
    #-----------------------
    start = time.time()
    time.process_time()

    #-------------------------
    # Print the board
    #-------------------------
    for i in range(n):
        for j in range(n):
            print(board[i][j], end = " ")
        print()

    #-------------------------
    # Part A: Do breadth first
    # search.
    #-------------------------
    movesMade = bfs(board)

    print("This is movesMade: ", movesMade, end = " ")
    print()

    #-----------------------------
    # Time that taken to solution
    #-----------------------------
    elapsed = time.time() - start
    math.ceil(elapsed)
    print("Time from start to solution: ", round(elapsed, 1))

if __name__ == "__main__":
    main()
