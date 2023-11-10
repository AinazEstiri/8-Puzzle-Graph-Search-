
import GameState 
import Search

#PLEASE CHECK these functions (change anything you think should be changed to match her guidelines)


#O(n^2) constant runtime 
def misplacedTile(state):
    misplaced = 0
    goalState = [[1,2,3],[4,5,6],[7,8,0]]
    for i in range(len(state)):
        for j in range(len(iter(state))):
            if state[i][j] != goalState[i][j] and state[i][j] != 0:
                misplaced += 1
    return misplaced


def euclideanDistance(state):
    distance = 0
    goalState = [[1,2,3],[4,5,6],[7,8,0]]
    for i in range(len(state)):
        for j in range(len(iter(state))):
            if state[i][j] != 0:
                tile = state[i][j]
                goalPosition = [(numIndex, row.index(tile)) for numIndex, row in enumerate(goalState) if tile in row][0]
                distance += ((i - goalPosition[0])**2 + (j - goalPosition[1])**2)**0.5
    return distance


#Search(startState, misplacedTile)
#Search(startState,  euclideanDistance)
