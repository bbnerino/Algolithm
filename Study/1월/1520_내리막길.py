import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs(y,x): # 함수에 들어오면
    if y == M-1 and x ==N-1: # 그값이 끝에 도착했다면?
        return 1             # visited[y][x]에 추가해준다.

    if visited[y][x] !=-1:  # 이미 들른 곳이면
        return visited[y][x]    #  그 값을 반환한다.

    if visited[y][x] ==-1:
        visited[y][x]=0         # 아직 안들른 곳이라면?
                                # 방문을 해준다.
        dy =[0,0,-1,1]
        dx =[1,-1,0,0]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<M and 0<=nx<N:
                if graph[ny][nx]<graph[y][x]:   # 다음 값이 현재 값보다 작다면?
                    visited[y][x]+= dfs(ny,nx)  # 현재 위치의 visited 값은 dfs(다음값) 으로 찾는다 .
    return visited[y][x]




M,N = map(int,input().split())
graph =[]
for _ in range(M):
    graph.append(list(map(int,input().split())))
visited =[[-1]*N for _ in range(M)]

print(dfs(0,0))