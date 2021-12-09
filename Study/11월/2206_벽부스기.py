import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque
import heapq
def bfs():
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    Q = []
    heapq.heappush(Q,[1,0,0])
    visit[0][0]=1
    while Q:
        cnt,y,x = heapq.heappop(Q)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M:
                if ny==N-1 and nx==M-1:
                    result.append(cnt+1)
                    return
                else:
                    if graph[ny][nx]==0 and visit[ny][nx]==0:
                        visit[ny][nx]=1
                        heapq.heappush(Q,[cnt+1,ny,nx])
                


N,M = map(int,input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,list(input().strip()))))

wall = deque() # 벽 위치 전부 넣는다
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            try: # 가지치기 
                if graph[i+1][j]==0 or graph[i-1][j]==0 or graph[i][j+1]==0 or graph[i][j-1]==0:
                    wall.append([i, j])
                else:
                    pass
            except:
                # wall.append([i,j])
                pass
result=[]



while wall:
    y,x = wall.popleft()
    graph[y][x]=0
    visit = [[0]*M for _ in range(N)]
    bfs()
    graph[y][x]=1
if result:
    print(max(result))
else:
    print(-1)
