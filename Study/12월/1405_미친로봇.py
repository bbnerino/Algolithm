import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

C,E,W,N,S = map(int,input().split()) # count, 동서남북 순
graph = [[0]*30 for _ in range(30)]  # 임의의 좌표를 만들어 준다
graph[15][15]=1                      # 중간지점이 내가 시작할 좌표
result =0                            # 최종 확률

def dfs(y,x,per,count):             # y좌표 , x좌표, 현재 확률, 남은차례
    global result
    dy = [0,0,1,-1]                 # 동서남북 순
    dx = [1,-1,0,0]

    if count==0:                    # 남은차례가 없다면
        result+= per                # 결과 넣고 끝내기
        return

    for i in range(4):              # 네방향 순회하면서
        ny = y+dy[i]
        nx = x+dx[i]
        if graph[ny][nx] == 0:      # 그 자리가 방문 안한 자리라면
            if i==0:                # j = 동서남북으로 갈 확률
                j = E/100
            elif i==1:
                j = W/100
            elif i==2:
                j = N/100
            elif i==3:
                j = S/100

            if j != 0:                   # j가 0이 아니라면
                graph[ny][nx] = 1        # 방문 해주고
                dfs(ny,nx,per*j,count-1) # dfs()
                graph[ny][nx]=0          # dfs가 끝나면 다시 방문 취소
dfs(15,15,1,C)
print(result)




