import sys
sys.stdin = open("./2023/1월/input.txt")


N,M = map(int,input().split())
graph = []
for _ in range(N):
  graph.append(list(map(int,input().split())))

result = 0
def bfs(START):
  global result 
  result+=1
  x_vector = [1,-1,0,0]
  y_vector = [0,0,1,-1]
  Q = [START]
  while Q:
    y,x = Q.pop(0)
    for i in range(4): 
      ny = (y+ y_vector[i])%N
      nx = (x+ x_vector[i])%M
      if graph[ny][nx] == 0:
        graph[ny][nx] = 1
        Q.append([ny,nx])

for i in range(N):
  for j in range(M):
    if graph[i][j] ==0:
      bfs([i,j])
print(result)

        