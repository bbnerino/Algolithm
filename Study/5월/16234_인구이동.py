import sys
from collections import deque
sys.stdin = open('input.txt')

N,L,R = map(int,input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

def move(y,x):
    Q = deque()
    Q.append([y,x])
    dy = [1,-1,0,0]
    dx = [0,0,-1,1]
    countries = [[graph[y][x], y, x]]
    while Q:
        y,x = Q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<N :
                if L <= abs(graph[ny][nx]-graph[y][x]) <= R:
                    if [graph[ny][nx],ny,nx] not in countries :
                        countries.append([graph[ny][nx],ny,nx])
                        Q.append([ny,nx])
    return countries

count = 0
more_change = True
while more_change: # 더 변경할 거리가 있는 지 확인
    if_change = False  # 이번 턴에 변경됐나?
    visited = [[0]*N for _ in range(N)]      # 이번턴에 변경됐던 값은 다시 안하게끔
    for i in range(N):
        for j in range(N):
            if i+1<N:  # 다음 값이 범위 내에 있을 경우
                if L <= abs(graph[i + 1][j] - graph[i][j]) <= R  and visited[i+1][j]==0: # 값 차이가 사이값이라면?
                    changelist = move(i, j) # 변경할리스트들 가져온다.
                    if_change = True    # '이번에 변경됐다'0
                    summ = 0
                    for c in changelist:
                        summ += c[0]
                    for c in changelist:
                        graph[c[1]][c[2]] = summ // len(changelist)
                        visited[c[1]][c[2]] = 1
                    continue
            elif j+1<N:
                if  L <= abs(graph[i][j] - graph[i][j + 1]) <= R:
                    changelist = move(i, j)
                    if_change = True
                    summ = 0
                    for c in changelist:
                        summ += c[0]
                    for c in changelist:
                        graph[c[1]][c[2]] = summ // len(changelist)
                        visited[c[1]][c[2]] = 1
                    continue

    if if_change :
        count+=1
    else: # 더 바꿔야하나?
        more_change = False

print(count)