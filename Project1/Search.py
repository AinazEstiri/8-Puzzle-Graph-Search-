from GameState import GameState
from queue import PriorityQueue
class Search:
    startState = None
    h = lambda x : 0
    
    def __init__(self, startState, h):
        self.startState = startState
        self.h = h
    
    #branching factor is 4 because we can move a state in four different directions
    #
    #O(b^d) may be influenced by the heuristic function h() and the efficiency of the getMoves()
    def search(self, display = False):
        frontier = PriorityQueue()
        frontier.put((self.h(self.startState), self.startState))
        checkedStates = set()
        inFrontier = set()
        expanded = 0
        maxNodes = 0
        numNodes = 0

        while not frontier.empty():
            currentNode = frontier.get()[1] #choose a leaf node and remove it from the frontier
            if display:
                print("Expanding best node with g(n) =", currentNode.depth, "and h(n) =", self.h(currentNode))
                print(currentNode)
                input()
           
            if currentNode.goalTest(): #if leaf node contains a goal state then return the solution
                return expanded, maxNodes, currentNode.depth, 
            checkedStates.add(currentNode) #add the node to the explored set

            #worst case scenario (add 4 new moves to frontier again from the top)
            for state in currentNode.getMoves(): #expand the chosen node
                if state not in checkedStates and state not in inFrontier: #only if not in the frontier or explored set
                    expanded += 1
                             #closest to the goal    fuest moves it
                    frontier.put((self.h(state) + state.depth, state)) #adding the resulting nodes to the frontier 
                    inFrontier.add(state)
                    numNodes = frontier.qsize()
                    maxNodes = max(numNodes, maxNodes)
        return None #if frontier empty then return failure