import sys
sys.stdin = open("input.txt")

from collections import deque      # 데큐 가져오기

N,M,K = map(int,input().split())   # 세로,가로 ,쓰레기 개수
graph= [[0]*M for _ in range(N)]   # 모든 위치 0으로 만들기
which = []                         # 쓰레기 위치

for _ in range(K):                 # 쓰레기 개수만큼
    r,c = map(int,input().split()) # 위치(y,x)
    graph[r-1][c-1]=1              # 쓰레기 있는 곳 1로 만들기
    which.append([r-1,c-1])        # 쓰레기 위치에 추가해주기


large = 0                         # 가장 큰 뭉치
def bfs(b,a):                     # bfs 탐색
    global large
    Q = deque()                   # queue 를 만들고
    Q.append([b,a])               # b,a를 추가해준다
    dy = [1,-1,0,0]               # y 네 방향 벡터값
    dx = [0,0,1,-1]               # x 네 방향 벡터값
    graph[b][a]=2                 # 쓰레기가 있는 곳은 뭉치(2)로 바꿔준다
                                  # -> visit 대신 지나간 곳은 2로 바꿔주기(뭉치)
    count = 1                     # 시작 뭉치=1로 시작

    while Q:                      # Q를 다 순회할 때 까지
        y,x = Q.popleft()         # 좌측 값을 뽑아서
        for i in range(4):        # 4방향 순회
            ny = y + dy[i]        # 다음 y 값
            nx = x + dx[i]        # 다음 x 값
            if 0<=ny<N and 0<=nx<M:            # x,y가 범위 내에 있다면
                if graph[ny][nx] == 1:         # 그 값이 쓰레기라면?
                    graph[ny][nx] = 2          # 뭉치로 바꾸기
                    count+=1                   # 뭉치 크기+1
                    large = max(large, count)  # 지금까지의 count가 가장 큰 뭉치인지 확인한다
                    Q.append([ny,nx])          # 다음 값 넣기



while which:             # 쓰레기 위치 전부를 순회하며
    b,a = which.pop()    # 하나씩 뽑아서
    if graph[b][a]==1:   # 그 값이 쓰레기라면?
                         # 뭉치(2)는 안됨X
        bfs(b,a)         # bfs
print(large)             # 가장 큰 뭉치 구하기


