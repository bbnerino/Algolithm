import sys
sys.stdin =open('input.txt')

N,M = map(int,input().split())
graph = []
score = {"W":0,"B":0}
for _ in range(M): # WMWWW 붙어 있는 글자 떼어주기
    graph.append(list(input()))

def dfs(y,x,team):
    global count
    ny = [0,0,-1,1]
    nx = [1,-1,0,0]
    graph[y][x] = "X"
    for i in range(4):
        dy = ny[i]+y
        dx = nx[i]+x
        if 0<=dy<M and 0<=dx<N :
            if graph[dy][dx] == team:
                flag = False
                count += 1
                dfs(dy,dx,team)

for i in range(M):
    for j in range(N):
        if graph[i][j] !="X":
            count = 1
            word = graph[i][j]
            dfs(i,j,word)
            score[word] += count**2
print(score['W'],score['B'])