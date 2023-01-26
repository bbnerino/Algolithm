import sys
sys.stdin = open("./2023/1월/input.txt")
import heapq

N = int(input())
graph  = []

for _ in range(N):
  graph.append(list(map(int,input().split())))

for i in range(N):
  for j in range(N):
    if graph[i][j]:
      graph[i][j]= -10
    if graph[i][j]==0:
      graph[i][j] = N*N
# 육지 -10 , 바다 = 0
def bfs(sy,sx):
  Q = []
  heapq.heappush(Q,[0,sy,sx])
  graph[sy][sx] = -11
  dy = [0,0,1,-1]
  dx = [1,-1,0,0]
  while Q:
    count,y,x = heapq.heappop(Q)
    for i in range(4):
      ny = dy[i] + y
      nx = dx[i] + x
      if 0<=ny<N and 0<=nx<N:
        if graph[ny][nx]==-10:
          graph[ny][nx]+= -11
          heapq.heappush(Q,[count,ny,nx])
          break
        else :
          if count+1 < graph[ny][nx]:
            graph[ny][nx] = count+1
            heapq.heappush(Q,[count+1,ny,nx])
  for i in range(N):
    print(graph[i])        

for i in range(N):
  for j in range(N):
    if graph[i][j]==-10:
      bfs(i,j)
      exit()


          
            
# bfs(0,0)

