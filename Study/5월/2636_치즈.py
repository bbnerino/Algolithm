import sys
from collections import deque

sys.stdin = open('input.txt')

N,M = map(int,input().split())
graph =[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

# 공기 0 치즈 1
# 접촉한 치즈 2

start = [0,0]  # 공기인 곳 한군데를 찾기 위한 로직
flag= False    # 찾으면 그만두기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            start = [i,j]
            flag = True
            break
    if flag==True:
        break


def find_rotten():  # 공기 부분을 모두 도는데 치즈를 만난다면  rotten이라는 곳에 쌓아두고
                    # 다음번에 전부 공기로 만들어 주기위함
    Q= deque()
    rotten = []
    visited = [[0] * M for _ in range(N)]
    visited[start[0]][start[1]] = 1
    Q.append(start)
    dy = [0,0,-1,1]
    dx = [1,-1,0,0]
    while Q :
        y,x =Q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<M: # 범위내에 있고
                if graph[ny][nx] ==0 and visited[ny][nx]==0: # 공기이면서 방문 X 면
                    visited[ny][nx] = 1 # 방문시켜주고
                    Q.append([ny,nx]) # 추가
                elif graph[ny][nx] == 1 and visited[ny][nx]==0: # 공기랑 만난 치즈면서 방문 X면
                    visited[ny][nx] = 1 # 방문 시켜주고
                    rotten.append([ny,nx]) # 썩는다
    return rotten

count = 0
last = 10000
while True:
    this_rotten = find_rotten() # 이번에 썩힐 치즈 리스트
    if len(this_rotten) == 0: # 썩힐 치즈가없다면? == 이미 다 없어진 것 => 전에꺼를 출력하며 마무리
        print(count)
        print(last)
        break
    else :     # 썩힐 치즈가 있다면
        for i,j in this_rotten: # 치즈들을 다 공기로 만들어 준다
            graph[i][j] = 0
        count += 1  # 차례를 넘기고 while 문을 반복시킨다.
        last =  len(this_rotten)