import sys
sys.stdin= open('input.txt')
from collections import deque
N = int(input())
graph = [[]for _ in range(N+1)]
score = list(range(N))
while True:
    a,b = map(int,input().split())
    if a==-1 :
        break
    else:
        graph[a].append(b)
        graph[b].append(a)

def bfs(start):
    Q = deque()
    visited = [False for _ in range(N+1)]
    visited[0] = True
    visited[start] = True
    Q.append(start)
    cnt = 0
    while Q :
        tmp = Q.popleft()
        flag= False
        for i in graph[tmp]:
            if visited[i] ==False:
                Q.append(i)
                visited[i] = True
                flag =True
        if flag:
            cnt+=1
    if False in visited:
        cnt = 0
    return cnt

small = 1000000
result =[]
for i in range(1,N+1):
    tmp = bfs(i)
    if tmp ==0:
        pass
    if score[tmp]<small:
        small = score[tmp]
        result = [i]
    elif score[tmp] == small:
        result.append(i)

print(small,len(result))
print(*result)

