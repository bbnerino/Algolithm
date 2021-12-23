import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

M,N = map(int,input().split())

graph = []
for _ in range(N):
    ls=list(map(int,input().rstrip()))
    graph.append(ls)

def bfs():
    global result,visited
    Q = []
    heapq.heappush(Q,[0,0,0])
    visited = [[10000]*M for _ in range(N)] # visited를 큰 값으로 만든다
                                            # 이 값은 벽을 몇개 부섰는지로 바꿀 수 있다.
    visited[0][0] = 1
    result= []

    while Q:
        wall,y,x = heapq.heappop(Q)
        if y==N-1 and x==M-1:           # 값이 우리가 찾는값이면
            result.append(wall)         # result에 넣어준다-> 한개일텐데 일단 넣어준다

        dy = [0,0,-1,1]
        dx = [1,-1,0,0]

        for i in range(4):          # 네방향 순회를 하면서
            ny = dy[i]+y
            nx = dx[i]+x
            if 0<=ny<N and 0<=nx<M:  # 범위내에 있다면?
                if graph[ny][nx]==0 and visited[ny][nx]>wall:
                    # 길이 있고, visited가 내가 지금 부슨 벽보다 크다면
                    visited[ny][nx]=wall    # visited를 부슨 벽 크기로 바꾼다.
                    heapq.heappush(Q,[wall,ny,nx])

                if graph[ny][nx]==1 and visited[ny][nx]>wall+1:
                    # 벽이라면 wall 대신 wall+1이 될 뿐 똑같은 로직이다.
                    visited[ny][nx] = wall+1
                    heapq.heappush(Q,[wall+1,ny,nx])

bfs()
print(min(result))
