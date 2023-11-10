from GameState import GameState
from searchAlgorthims import *

def finalResultStatement(expantionTotal, queueMax, goalDepth):
    print(f"To solve this problem the search algorthim expanded a total of {expantionTotal} nodes.")
    print(f"The maximum number of nodes in the queue at any one time: {queueMax}.")
    print(f"The depth of the goal node was {goalDepth}.")

Trivial = GameState.GameState([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
])

VeryEasy = GameState.GameState([
    [1, 2, 3],
    [4, 5, 6],
    [7, 0, 8]
])

Easy = GameState.GameState([
    [1, 2, 0],
    [4, 5, 3],
    [7, 8, 6]
])

Doable = GameState.GameState([
    [0, 1, 2],
    [4, 5, 3],
    [7, 8, 6]
])

OhBoy = GameState.GameState([
    [8, 7, 1],
    [6, 0, 2],
    [5, 4, 3]
])

Impossible = GameState.GameState([
    [1, 2, 3],
    [4, 5, 6],
    [8, 7, 0]
])

TestCases = [Trivial, VeryEasy, Easy, Doable, OhBoy]
TestCasesNames = ['Trivial', 'VeryEasy', 'Easy', 'Doable', 'OhBoy']

def h(x):
    return 0

Algorithms = [h, misplacedTile, euclideanDistance]

def allTestCases():
    for state in range(len(TestCases)):
        print(TestCasesNames[state])
        for algorithm in Algorithms:
            print(algorithm.__name__)
            expantionTotal, queueMax, goalDepth= Search.Search(TestCases[state], algorithm).search(False)
            finalResultStatement(expantionTotal, queueMax, goalDepth)
        print()