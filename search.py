import time



#TODO: Build Graph based on n^2
#------------------------
# This function builds
# The array matrix (grid)
# based off n.
#------------------------
def buildGrid(gridNumber):
    grid = array[n][n]




#TODO: Choose search method: Breadth-first, Hill climbing, or Simulated anneling search
def bfs(grid):
    #TODO: Do Breadth-first Search
    return something

def hcs(grid):
    #TODO: Do Hill-climbing Search
    return something

def sa(grid):
    #TODO: Simulated-anneling Searh
    return something


#TODO: If breadth-first n=1-6 print number of solutions & visual graph, for n=7-20 only pring number of solutions
#      if Hill-climbing & SA (visual rep up to n=8)
#TODO: Cost function determining the distance to solutions





###TODO: Function asking for n
#------------------------
# Main Function asking
# for the initial input
#------------------------

def main():

    print("Please enter number for grid")
    n = int(input())

    buildGrid(n)

    #TODO: Record time to solution
    #-----------------------
    # Start time to solution
    #-----------------------
    start = time.time()
    time.clock()


    #-----------------------------
    # Time that taken to solution
    #-----------------------------
    elapsed = time.time() - start

if __name__ == "__main__":
    main()
