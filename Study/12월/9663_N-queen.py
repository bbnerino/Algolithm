import sys
sys.stdin = open('input.txt')

N = int(input())



def check(y,x):
    checklist = set()
    for i in range(y, N):
        checklist.add((i,x))
        # visited[i][x] = 1

    for j in range(x + 1, N):
        checklist.add((y,j))
        # visited[y][j] = 1

    dx = [1, -1]
    for j in range(N):
        for i in range(2):
            ny = y + j
            nx = x + j * dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                checklist.add((ny,nx))
                # visited[ny][nx] = 1
    return checklist


def dfs(y,x):
    global result
    if y == N-2:
        result+=1

    for i in range(N):
        if visited[y+1][i]==0:
            checklist =check(y+1,i)
            for p,q in checklist:
                visited[p][q]= 1
            dfs(y+1, i)
            for p,q in checklist:
                if p >= y:
                    visited[p][q]= 0
result =0

for i in range(N):
    visited = [[0] * N for _ in range(N)]
    checklist=check(0,i)
    for p,q in checklist:
        visited[p][q]=1
    dfs(0, i)
    for p,q in checklist:
        visited[p][q]=0



print(result)