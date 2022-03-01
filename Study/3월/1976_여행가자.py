import sys
sys.stdin = open('input.txt')
from collections import deque

N = int(input())
M = int(input())
graph = [[]for _ in range(N+1)]
for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(len(tmp)):
        if tmp[j]==1:
            graph[i+1].append(j+1)
travel = list(map(int,input().split()))

def bfs():
    Q = deque()
    visited = [0 for _ in range(N+1)]
    visited[travel[0]]= 1
    Q.append(travel[0])
    while Q :
        s = Q.popleft()
        for i in graph[s]:
            if visited[i]==0:
                visited[i] = 1
                Q.append(i)
    return visited

visited = bfs()
if travel:
    result = "YES"
    for i in travel:
        if visited[i] == 0:
            result = "NO"
else:
    result="NO"

print(result)
