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
    dist = [0] * (N+1) # 시작 노드부터 거리
    while Q :
        # 한명씩 확인하면서 node의 길이를 구한다
        tmp = Q.popleft()
        for i in graph[tmp]:
            if not visited[i] : # 아직 친구등록이 안되어있으면
                Q.append(i) # Q 추가 해주고
                visited[i] = True  # 친구 등록해준다
                dist[i] = dist[tmp] + 1 # 1->3 -> 2  ?? 2가된다 .
    return dist

small = 50
result =[]
for i in range(1,N+1):
    tmp = max(bfs(i))
    if score[tmp]<small:
        small = score[tmp]
        result = [i]
    elif score[tmp] == small:
        result.append(i)

print(small,len(result))
print(*result)

