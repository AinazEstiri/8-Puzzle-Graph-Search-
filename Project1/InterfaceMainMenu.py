from searchAlgorthims import *
from Search import Search
from GameState import GameState
from TestCases import allTestCases

def finalResultStatement(expantionTotal, queueMax, goalDepth):
    print(f"To solve this problem the search algorthim expanded a total of {expantionTotal} nodes.")
    print(f"The maximum number of nodes in the queue at any one time: {queueMax}.")
    print(f"The depth of the goal node was {goalDepth}.")

def mainMenu():
    
####this bit gets user input for puzzle
    print("Welcome to 862192636, 862179537, 862183050, and  862243371 8 puzzle solver.\n")
    while True:
        userInput = input('Type "1" to use a default puzzle, or "2" to enter your own puzzle, or "3" for all test cases\n')
        if userInput == '1':
            #IDEK WHAT IT WOULD BE YET!!!!! I think its the puzzle one on page 2?
        
            firstRow = "1 0 3"
            firstRow= [int(num) for num in firstRow.split()] #makes rows into vector [#,#,#]
            secondRow = "4 2 6"
            secondRow= [int(num) for num in secondRow.split()] #makes rows into vector [#,#,#]
            thirdRow = "7 5 8"
            thirdRow= [int(num) for num in thirdRow.split()] #makes rows into vector [#,#,#]
            
            #makes a [[#,#,#],[#,#,#],[#,#,#]] matrix format
            matrix= [firstRow,secondRow,thirdRow]
            break 

        elif userInput == '2':
            print("Enter your puzzle, use a zero to represent the blank")
            firstRow = input("Enter the first row, use a space between numbers \n")
            firstRow= [int(num) for num in firstRow.split()] #makes rows into vector [#,#,#]
            secondRow = input("Enter the second row, use a space between numbers \n")
            secondRow= [int(num) for num in secondRow.split()] #makes rows into vector [#,#,#]
            thirdRow = input("Enter the third row, use a space between numbers \n")
            thirdRow= [int(num) for num in thirdRow.split()] #makes rows into vector [#,#,#]
            
            #makes a [[#,#,#],[#,#,#],[#,#,#]] matrix format
            matrix= [firstRow,secondRow,thirdRow]
            break
        
        elif userInput == '3':
            allTestCases()
            return

        else:
            print("Invalid input, please try again")

   

####This bit get user to pick a search algorithm and solves the puzzle
    goalMatrix= [[1,2,3],[4,5,6],[7,8,0]] #this is the goal state matrix we want to reach
    state = GameState(matrix)
    def h(state):
        return 0

    while True:
        algoChoice = input("Enter your choice of algorithm \n   Uniform Cost Search (1) \n   A* with the Misplaced Tile heuristic (2) \n   A* with the Euclidean distance heuristic (3)")
        if algoChoice == '1':
            expantionTotal, queueMax, goalDepth= Search(state, h).search(True)
            break
        elif algoChoice == '2':
            expantionTotal, queueMax, goalDepth= Search(state,misplacedTile).search(True)
            break
        elif  algoChoice =='3':
            expantionTotal, queueMax, goalDepth= Search(state,euclideanDistance).search(True)
            break
        else:
            print("Invalid input, please try inputs '1' or '2' or '3'")


####Prints the final result paragraph
    finalResultStatement(expantionTotal, queueMax, goalDepth)

    
mainMenu()



