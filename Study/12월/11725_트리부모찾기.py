import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
input =sys.stdin.readline

N= int(input())
graph = [[]for _ in range(N+1)]

# 트리입력 받는 법
# 트리 갯수만큼 빈칸을 만들고 s,e방향 맞춰서 넣어주기
for _ in range(N-1):    # 모든 입력 받기
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

tree = [[]for _ in range(N+1)] # 부모노드 찾는 트리
visited =[0]*(N+1)             # 간 곳은 안가게 만들어
                               # 순환하지 않게 하기

def dfs(n):                     # 최상단 노드인 1에서 시작해서
                                # 트리가 내려간다
    visited[n]=1                # 현재 위치 방문처리 해주고

    for i in graph[n]:         # 그 위치에서 내려가는 값 모든값이
        if visited[i]==0:       # 방문을 안했다면
            tree[i].append(n)   # 트리 추가해주기 (자식에서 부모로 올라가는값)
            dfs(i)              # dfs 들어가기

dfs(1)
for t in tree:
    if t:
        print(*t)