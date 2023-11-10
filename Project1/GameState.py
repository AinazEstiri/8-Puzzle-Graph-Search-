"""
GameState object represents one possible state of the board.
GameState() takes a 2 dimensional list and uses 0 to represent the blank space
goalTest() returns True if the board is in a goal state
moveLeft(), moveRight(), moveUp(), moveDown() return the new GameState when the action is completed, or None if the move is invalid (might make these private)
getMoves() returns the list of reachable states from the current one
h() is a virtual function to represent the heuristic offset
"""
from collections import deque
from copy import deepcopy
class GameState:
  state = []
  blankPos = (0,0)
  parent = None
  depth = 0

  def __init__(self, state):
    self._i = 0
    self.state = state
    for row in range(0, len(state)): #get blankPos 
      for item in range(0, len(state[row])):
        if state[row][item] == 0: self.blankPos = (item, row)


  def __str__(self):
      toStr = ""
      for line in self.state:
        toStr += str(line) + '\n'
      return toStr


  def __eq__(self, rhs):
      if rhs.__class__ == GameState: return self.state == rhs.state
      else: return False


  def __lt__(self, rhs): 
    return False #This is a workaround for the queue. If two items have the same priority it doesn't matter which comes first.

  def __len__(self):
    return len(self.state)
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if self._i >= len(self.state):
      raise StopIteration
    next_item = self.state[self._i]
    self._i += 1
    return next_item
  
  # allows for indexing of GameState object
  def __getitem__(self, index):
    return self.state[index]
    

  def __hash__(self):
    hash = 0
    offset = 1
    for row in self.state:
      for item in row:
        hash += item * offset
        offset *= 9
    return hash


  def goalTest(self):
    tileOrder = deque(range(1, len(self.state)*len(self.state[0])))
    for row in self.state:
      for item in row:
        if item == 0: continue
        elif item == tileOrder[0]: tileOrder.popleft()
        else: return False
    return True


  def moveLeft(self):
    return self.__move((-1,0))
  
  
  def moveRight(self):
    return self.__move((1,0))
  
  
  def moveUp(self):
    return self.__move((0,-1))
  
  
  def moveDown(self):
    return self.__move((0,1))


  def getMoves(self):
    possibleMoves = []
    for func in [self.moveLeft, self.moveRight, self.moveUp, self.moveDown]:
      if func() != None: possibleMoves.append(func())
    return possibleMoves


  def h(self):
    pass


  def __swapCells(self, cell1, cell2):
    tmp = self.state[cell1[1]][cell1[0]]
    self.state[cell1[1]][cell1[0]] = self.state[cell2[1]][cell2[0]]
    self.state[cell2[1]][cell2[0]] = tmp


  def __move(self, direction): #private function for generalized move logic
    newGameState = deepcopy(self)
    newGameState.blankPos = (newGameState.blankPos[0] + direction[0], newGameState.blankPos[1] + direction[1])
    if newGameState.blankPos[0] < 0 or newGameState.blankPos[0] >= len(self.state[0]): return None
    if newGameState.blankPos[1] < 0 or newGameState.blankPos[1] >= len(self.state): return None #out of bounds checking
    newGameState.__swapCells(self.blankPos, newGameState.blankPos)
    newGameState.parent = self
    newGameState.depth = self.depth + 1
    return newGameState
    