# this is an example of creating a simple game based on turns and strategy, using very basic techniques. 
# in this game, the player must take boxes and defend keep zombies away. The player can move boxes, but not zombies or walls.
# Wall = x or ■
# Zombie = z or ☻
# Player = p or ☺
# Boxes = o or □

from random import randint
from random import choice

def createSquareMap(dimension, boxes, zombies):
  arr = [["+" for i in range(dimension)] for j in range(dimension)]  
  
  #create external walls
  for i in range(dimension):
    arr[0][i] = "■"
    arr[i][0] = "■"
    arr[dimension-1][i] = "■"
    arr[i][dimension-1] = "■"

  # add some walls
  for i in range(1,dimension-1):
    for j in range(1,dimension-1):
      if randint(0,8)==0:
        arr[j][i] = "■"


  # create internal walls
  for i in range(dimension-1):
    for j in range(dimension-1):
      if arr[i][j] == "■":
        rand = randint(0,3) 
        if rand==1:
          arr[i][j+1] = "■"
        elif rand==2:
          arr[i+1][j] = "■"

  #liberate near space
  arr[1][2] = "+"
  arr[2][1] = "+"

  # add boxes
  for i in range(boxes+1):
    arr[randint(1,dimension-2)][randint(1,dimension-2)] = "□"


  # add player
  arr[1][1] = "☺"

  # add zombie
  i = 0
  while i<zombies:
    py = i//(dimension-2)
    px = i%(dimension-2)
    arr[dimension-2-py][dimension-2-px] = "☻"
    i+=1

  return arr

def printMap(arr):
  print("-----")
  for row in arr:
    print(row)

# zombie movement: roam free
def roamFree(x,y,arr):
  direction = randint(0,4)
  if direction == 1:
    if arr[y+1][x] == "+":
      arr[y+1][x], arr[y][x] = "☻", "+"
    elif arr[y+1][x] == "☺":
      arr[y+1][x] = "☻"
  elif direction == 2:
    if arr[y][x+1] == "+":
      arr[y][x+1], arr[y][x] = "☻", "+"
    elif arr[y][x+1] == "☺":
      arr[y][x+1] = "☻"
  elif direction == 3:
    if arr[y-1][x] == "+":
      arr[y-1][x], arr[y][x] = "☻", "+"
    elif arr[y-1][x] == "☺":
      arr[y-1][x] = "☻"
  elif direction == 4:
    if arr[y][x-1] == "+":
      arr[y][x-1], arr[y][x] = "☻", "+"
    elif arr[y][x-1] == "☺":
      arr[y][x-1] = "☻"
  return arr

# move player
def movePlayer(x,y,arr,direction):  
  if direction == "r":
    newX, newY = x+1, y
  elif direction == "l":
    newX, newY = x-1, y
  elif direction == "u":
    newX, newY = x, y-1
  elif direction == "d":
    newX, newY = x, y+1
  
  if arr[newY][newX] == "+":
    arr[newY][newX], arr[y][x] = "☺", "+"
    return True
  elif arr[newY][newX] == "□":
    if moveBox(newX,newY,arr,direction):   
      arr[newY][newX], arr[y][x] = "☺", "+"
      return True
  return False

# move box
def moveBox(x,y,arr,direction):
  newX, newY = x, y
  if direction == "r":
    newX, newY = x+1, y
  elif direction == "l":
    newX, newY = x-1, y
  elif direction == "u":
    newX, newY = x, y-1
  elif direction == "d":
    newX, newY = x, y+1

  if arr[newY][newX] == "+":
    arr[newY][newX] = "□"
    return True
  else:
    return False

print("--- ZOMBIE SURVIVAL GAME ---")
print("Instructions: r -> move right; l -> move left; u -> move up; d -> move down")
print('Select a number for size of maze:')
dimension = int(input())
print('Select the number of boxes:')
boxes = int(input())
print('Select the number of zombies:')
zombies = int(input())
print('GAME START:')



gameMap = createSquareMap(dimension,boxes,zombies)
# gameMap = createSquareMap(10,1,1)
printMap(gameMap)

turn = 1
playerX = 1
playerY = 1
while True:
  # See winning condition
  # if win, break, else continue
  print("Turn: " + str(turn))
  direction = input()
  if movePlayer(playerX,playerY,gameMap,direction):
    if direction == "r":
      playerX, playerY = playerX+1, playerY
    elif direction == "l":
      playerX, playerY = playerX-1, playerY
    elif direction == "u":
      playerX, playerY = playerX, playerY-1
    elif direction == "d":
      playerX, playerY = playerX, playerY+1
  # move player
  # move zombie
  for i in range(1,dimension-1):
    for j in range(1,dimension-1):
      if gameMap[i][j] == "☻":
        gameMap = roamFree(i,j,gameMap)
#      elif gameMap[i][j] == "☺":
        #gameMap = movePlayer(i,j,gameMap,movement)
#        gameMap = movePlayer(i,j,gameMap,movement)
  
  turn+=1
  printMap(gameMap)

  # update map



