import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

R,C,T = map(int,input().split()) # 입력받기
graph =[]
for _ in range(R):
    ls =[]              # 한 글 자 씩 받 는 법
    ls.extend(input())
    if '\n' in ls:      # 마지막에 띄워쓰기가 있다면
        ls.remove('\n') # 지워주고
    graph.append(ls)    # 그 리스트를 넣어준다

gahee = [0,0]           # 가희가 있는 곳
for i in range(R):
    for j in range(C):
        if graph[i][j]=='G':
            graph[i][j]='.'     # 찾아서 빈 곳으로 만들어 주고
            gahee = [i,j]       # 위치를 저장한다.


visit = [[0]*C for _ in range(R)]   # 방문 처리용
visit[gahee[0]][gahee[1]] = 1       # 가희를 방문처리 먼저 해주기

result = []                     # 결과 창
def dfs(y,x,time,potato,visit): # dfs 를 돌면서 (내위치,남은기회,먹은개수,방문유무확인용)
    if time == 0:               # 갈수있는 기회가 없다면
        result.append(potato)   # 먹은개수를 결과에 넣는다
        return
    dy = [0,0,1,-1]             # 네방향 순회하면서
    dx = [1,-1,0,0]
    for i in range(4):
        ny,nx = dy[i]+y , dx[i]+x
        if 0<=ny<R and 0<=nx<C: # 범위내에있고

            if graph[ny][nx]=='.' and visit[ny][nx]==0: # 길이 열려있고 방문 안했다?
                visit[ny][nx]=1     # 방문 시키고
                dfs(ny,nx,time-1,potato,visit)  # dfs 순회를 하는데
                visit[ny][nx]=0     # 순회가 끝나면 방문처리철회

            if graph[ny][nx]=='S' and visit[ny][nx]==0: # 고구마라면?
                graph[ny][nx]='.'   # 먹었다! 먹은자리 비우기

                newvisit = [[0]*C for _ in range(R)]    # 중요한 로직
                # 고구마를 먹고나면 모든 방문 처리를 다 없애서 다시 돌아갈 수 있도록 만들기
                dfs(ny,nx,time-1,potato+1,newvisit) # 새로운 visit를 넣어준다
                graph[ny][nx]='S'   # 고구마 다시 생기기


dfs(gahee[0],gahee[1],T,0,visit)
if len(result)==0:      # 이거 때문에 valueerror 났었음
    print(0)            # count가 남았는데 끝나면 result가 비게된다.
else:
    print(max(result))  # 최고값 구해주기