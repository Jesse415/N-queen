import numpy as np
import math
import copy
import time
import collections


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
                k+=1

    return movesMade

def bfsPrunning(board, n):
    #-----------------------
    # Deque meant to act as
    # a queue - FIFO
    #-----------------------
    movesMade = collections.deque()
    updateBoard = []
    i = 0

    #------------------------------
    # for loop to place Queen in
    # every spot in i=0 and add
    # to deque/queue movesMade
    #------------------------------
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
        temp = len(movesMade)
        check = temp*n
        count = 0
        while k < check:
                updateBoard = movesMade.popleft()

                for j in range(len(updateBoard[i])):
                    if updateBoard[i][j] == '-':
                        updateBoard[i][j] = 'Q'
                        if isMoveValid(updateBoard, n) is True:
                            movesMade.append(copy.deepcopy(updateBoard))
                            count += 1
                        updateBoard[i][j] = '-'
                    k+=1

    return movesMade


#--------------------------
# Function for prunning
# to check if the next move
# made is a valid move
#--------------------------
def isMoveValid(boardToCheck, n):
    for y in range(len(boardToCheck)):
        for x in range(len(boardToCheck[y])):

            #--------------
            # Found a queen
            #--------------
            if boardToCheck[y][x]=='Q':

                #----------------------
                # Check for column up
                #----------------------
                for j in range(y+1,n):
    	            if boardToCheck[j][x] == 'Q':
      	                return False

                #--------------------------
                # Check Diagonal Left up
                #--------------------------
                for a,b in zip(range(x-1,-1,-1),range(y+1,n,1)):
    	            if boardToCheck[b][a] == 'Q':
      	                return False

                #-----------------------------
                # Check Diagonal Right up
                #-----------------------------
                for a,b in zip(range(x+1,n),range(y+1,n,1)):
    	            if boardToCheck[b][a] == 'Q':
      	                return False

    return True


def vetForSolution(checkBoard, n):

    if n == 1:
        return True

    else:
        for y in range(len(checkBoard)):
            for x in range(len(checkBoard[y])):
                #-------------
                # Found a queen
                #-------------
                if checkBoard[y][x]=='Q':

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
    i=0

    #-----------------------
    # Input from user
    #-----------------------
    print("Please enter number for grid")
    n = int(input())

    #-----------------------
    # Builds the board needed
    # based on n
    #-----------------------
    board = np.full((n,n), '-')

    print("""
    (1)For Breadth First Search\n
    (2)For Breadth First Search with pruning\n""")

    x = int(input())

    #-----------------------
    # Start time to solution
    #-----------------------
    start = time.time()
    time.process_time()

    while x == 1 or x == 2:
        #-------------------------
        # Part A: Do breadth first
        # search add it to tree
        #-------------------------
        if x == 1:
            movesMade = bfs(board, n)

            for m in movesMade:
                if vetForSolution(m, len(m)):
                    solutions.append(m)

        #----------------------------
        # Part A(b): Do breadth first
        # search with Prunning
        #----------------------------
        elif x == 2:
            solutionPrunning = bfsPrunning(board, n)

            for y in range(len(solutionPrunning)):
                solutions.append(copy.deepcopy(solutionPrunning))

        else:
            print("Invalid selection. Closing program")
        break

    #--------------------
    # Stop time so not
    # to include printing
    # solutions
    #--------------------
    elapsed = time.time() - start

    if n < 7:
        #----------------------------
        # Print every branch of tree
        #----------------------------
        if len(solutions) > 0:
            for i in range(len(solutions)):
                for j in range(len(solutions[i])):
                    print(solutions[i][j], end = " ")
                    print()
                print()
            print("Number for Solutions: ", i+1)

        else:
            print("There are NO solutions")
    else:
        i = len(solutions)+1
        print("There are", i, "Solutions")


    #-----------------------------
    # Time that taken to solution
    #-----------------------------
    minutes = int(elapsed//60)
    hours = int(elapsed // 3600)
    #math.ceil(elapsed)
    print("Time: H:", hours,"M:",minutes,"S:",(round(elapsed, 4))%60)

if __name__ == "__main__":
    main()
