import copy
def checkShape(board, coords, x, y):
  coords1 = copy.deepcopy(coords)
  board1 = copy.deepcopy(board)
  touched = False
  
  for coord in coords1:
    coord[0] += x
    coord[1] += y
    if coord[0] > 9 or coord[0] < 0 or coord[1] > 13 or coord[1] < 0:
      return False, board1
      
    if board1[coord[1]][coord[0]] != 0:
      return False, board1

    for x1 in range(-1, 2):
      for y1 in range( -1, 2):
        if abs(x1) + abs(y1) == 1:
          if coord[0] + x1 < 10 and coord[0] + x1 >= 0 and coord[1] + y1 < 13 and coord[1] + y1 >= 0:
            if board[coord[1] + y1][coord[0] + x1] == 1:
              touched = True
              
  for coord in coords1:
    board1[coord[1]][coord[0]] = 1
  return touched, board1 

shapes = [["A", [[0,0],[0,1],[1,1],[0,2],[0,3]]],
          ["F", [[0,1],[1,0],[2,0],[1,1],[1,2]]],
          ["G", [[2,1],[1,0],[0,0],[1,1],[1,2]]],
          ["I", [[0,0],[0,1],[0,2],[0,3],[0,4]]],
          ["L", [[0,0],[0,1],[0,2],[0,3],[1,3]]],
          ["J", [[1,0],[1,1],[1,2],[1,3],[0,3]]],
          ["N", [[0,1],[1,1],[1,0],[0,2],[0,3]]],
          ["M", [[1,1],[0,1],[0,0],[1,2],[1,3]]],
          ["P", [[1,1],[0,1],[0,0],[1,0],[0,2]]],
          ["Q", [[1,1],[0,1],[0,0],[1,0],[1,2]]],
          ["T", [[0,0],[1,0],[2,0],[1,1],[1,2]]],
          ["U", [[0,0],[0,1],[1,1],[2,1],[2,0]]],
          ["V", [[0,0],[0,1],[0,2],[1,2],[2,2]]],
          ["W", [[0,0],[0,1],[1,1],[1,2],[2,2]]],
          ["X", [[1,0],[0,1],[1,1],[2,1],[1,2]]],
          ["Z", [[0,0],[1,0],[1,1],[1,2],[2,2]]],
          ["S", [[2,0],[1,0],[1,1],[1,2],[0,2]]],
          ["Y", [[1,0],[1,1],[0,1],[1,2],[1,3]]],
         ]
board=[[0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0]]

shapeI = [1, 1]
a = input("")
for i in range(2):
  for j in range(len(shapes)):
    if shapes[j][0] == a[i]:
      shapeI[i] = j

x = 4
y = 5
for coord in shapes[shapeI[0]][1]:
  board[coord[1]+y][coord[0]+x] = 1
  
all = []
for x1 in range(10):
  for y1 in range(13):
    touched, board1 = checkShape(board, shapes[shapeI[1]][1], x1, y1)
      
    if touched:
      columns = []
      for x in range(len(board1[0])):
        one = False
        for y in range(12):
          if board1[y][x] == 1:
            one = True
            break
        if one == False:
          columns.append(x)

      for x in range(len(columns)-1, -1, -1):
        for y in range(12):
          board1[y].pop(columns[x])      
      
      for i in range(len(board1)-1, -1, -1):
        if 1 not in board1[i]:
          board1.pop(i)

      all.append(copy.deepcopy(board1))

for board in all:
  for line in board:
    print(line)
  print("WWWWW")

for i in range(len(all)-1, -1, -1):
  if all.index(all[i]) != i:
    all.pop(i)

print(len(all))
