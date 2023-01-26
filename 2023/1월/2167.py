import sys
sys.stdin = open("./2023/1월/input.txt")

N,M = map(int,input().split())
graph = []
for _ in range(N):
  graph.append(list(map(int,input().split())))

T = int(input())
for ts in range(T):
  y1,x1,y2,x2 = map(int,input().split())
  result = 0
  for i in range(y1-1,y2):
    for j in range(x1-1,x2):
      result += graph[i][j]

  print(result)