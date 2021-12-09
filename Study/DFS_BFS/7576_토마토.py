import sys
sys.stdin= open('input.txt')

from collections import deque
M,N = map(int,input().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

ripe = deque()       # 1 위치 찾기
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            ripe.append([i,j,0]) # 0=? count를 나타낼 자리

def bfs():
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    countlist=[]    #
    while ripe:
        s = ripe.popleft()    # 하나를 뽑아서
        countlist.append(s[2])# 나중에 찾기 쉽게끔 list에 count를 넣어준다
        for i in range(4):
            ny = dy[i]+s[0]
            nx = dx[i]+s[1]

            if 0<=ny<N and 0<= nx <M:   # 범위내 라면
                if graph[ny][nx]==0:    # 토마토가 있다면
                    graph[ny][nx]=1     # 익게 만들고
                    ripe.append([ny,nx,s[2]+1]) # queue에 넣어주는데 count+=1 해서 넣어준다

    for line in graph:  # 전체에서
        if 0 in line:   # 0이 남아있다면
            print(-1)   # -1를 출력하고
            return      # 함수끝낸다

    print(max(countlist)) # 0이 없다면 countlist에서 가장 큰값이 최종 시간이다.
bfs()