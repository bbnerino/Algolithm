import sys
sys.stdin = open('input.txt')
from collections import deque

N,M,T = map(int,input().split())

graph =[]
for _ in range(N):
    tmp = deque(map(int, input().split()))
    graph.append(tmp)

visited = [[1000]*M for _ in range(N)]

for _ in range(T):
    X,D,K = map(int,input().split())
    if D ==1:
        while X-1<N:
            graph[X-1].rotate(-K)
            X = 2 * X


    if D ==0:
        while X-1<N:
            graph[X-1].rotate(K)
            X = 2 * X
    dy = [0,1]
    dx = [1,0]

    flag= False
    for i in range(N):
        for j in range(M):
            num = graph[i][j]
            for k in range(2):
                ny = dy[k] + i
                nx = (dx[k] + j)%M
                if ny<N :
                    if graph[ny][nx] == num:
                        flag= True
                        visited[ny][nx]=0
                        visited[i][j] = 0
                    else:
                        if visited[i][j]!=0:
                            visited[i][j] = num
    result = 0
    cnt = 0
    avr=0
    for g in visited:
        tmp = 0
        for i in g:
            if i>0:
                cnt+=1
            tmp += i
        result += tmp

    if flag == False:
        avr = result / cnt
        for i in range(N):
            for j in range(M):
                if visited[i][j]>=avr:
                    visited[i][j] += 1
                else:
                    visited[i][j] -= 1
        result = 0
        cnt = 0
        for g in visited:
            tmp = 0
            for i in g:
                tmp += i
            result += tmp

    print(visited)

    print(result)