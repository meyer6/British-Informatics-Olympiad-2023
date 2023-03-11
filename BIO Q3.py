from collections import deque
import copy

def solve(pegs, target): 
  options = deque()
  options.append((pegs, 0))
  maxPast = []
  while True:
    current, step = options.popleft()
    for i in range(4):
      for j in range(4):
        if i != j and len(current[i])!=0 :
          p = copy.deepcopy(current)
          p[j] += p[i][-1]
          p[i] = p[i][:-1]
          if p not in maxPast:
            if p == target:
              return step + 1
            options.append((p, step + 1))
            maxPast.append(p)

a,b,c,d = input("").split(" ")
pegs = [a, b, c, d]
pegs = [peg.replace("0", "") for peg in pegs]

a,b,c,d = input("").split(" ")
target = [a, b, c, d]
target = [peg.replace("0", "") for peg in target]

print(solve(pegs, target))










# from collections import deque
# import copy

# def solve(pegs, target): 
#   options = deque()
#   options.append((pegs, 0))
#   maxPast = []
#   count = 0
#   while True:
#     current, step = options.popleft()
#     if step == 4:
#       print(current)
#       count+=1
#     for i in range(4):
#       for j in range(4):
#         if i != j and len(current[i])!=0 :
#           p = copy.deepcopy(current)
#           p[j] += p[i][-1]
#           p[i] = p[i][:-1]
#           if p not in maxPast:
#             if p == target:
#               print(count)
#               return step + 1
#             options.append((p, step + 1))
#             if step == 3:
#               maxPast.append(p)

# a,b,c,d = input("").split(" ")
# pegs = [a, b, c, d]
# pegs = [peg.replace("0", "") for peg in pegs]

# a,b,c,d = input("").split(" ")
# target = [a, b, c, d]
# target = [peg.replace("0", "") for peg in target]

# print(solve(pegs, target))







