import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
r,c,d = map(int,input().split())
# r,c 좌표 , d = 바라보는 방향
# 0 북 1 동 2 남 3 서
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

dy = [-1,0,1,0]
dx = [0,1,0,-1]


def dfs(y,x,dir):   # dfs와 동일하다
    global cnt
    if graph[y][x]==0: # 쓰레기면
        graph[y][x]=2   # 청소해주고
        cnt+=1          # 갯수 추가

    for i in range(4):  # 4방향을 도는데 순서가 있다
        nd = (dir-1)%4 # 원래 -1 인데 0이하면 %4해주면 된다
        ny = dy[nd]+y   # 다음 값y,x
        nx = dx[nd]+x
        if 0<=ny<N and 0<=nx<M:
            if graph[ny][nx]==0:    # 다음이 쓰레기라면
                dfs(ny,nx,nd)       # dfs 를 돌린다
                return              # 뒤의 순서는 생각안해준다

        dir = nd    # 네방향 다 없다면 마지막의 nd 방향을 기록해준다
    ny = dy[dir-2] + y  # 뒤 방향
    nx = dx[dir-2] + x
    if 0<=ny<N and 0<=nx<M:
        if graph[ny][nx]==1:    # 뒤가 벽이라면
            return  # 끝낸다
    dfs(ny,nx,dir)  # 2거나 0이면 또 들어간다.

cnt = 0
dfs(r,c,d)
print(cnt)

