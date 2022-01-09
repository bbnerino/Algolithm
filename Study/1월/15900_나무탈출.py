import sys
sys.stdin = open('input.txt')

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph =[[]for _ in range(N+1)]
for _ in range(N-1):    # 양방향 트리 만들어주기
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [0]*(N+1)
result  = 0
def dfs(start,cnt):
    global result
    visited[start] = 1 # 방문을 시켜주고
    is_leaf = True      # 노드에서 더이상 갈 곳이 없으면? (leaf)
    for i in graph[start]:  # 노드에서 다른 노드로 가는걸 확인
        if visited[i] ==0:  # 방문이 안되어있다면
            dfs(i,cnt+1)    # 더 들어가기 ( cnt로 길이 표시)
            is_leaf = False # 리프노드가 아니다 표시

    if is_leaf:             # 리프노드라면
        result +=cnt        # result에 넣어주면서 끝내기


dfs(1,0)
if result%2 ==0:        # 홀수면 지고 짝수면 이긴다.
    print('No')
else:
    print('Yes')
