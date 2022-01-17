import sys
sys.stdin =open('input.txt')

N = int(input())

graph = [[]for _ in range(N)]       # 그래프 형태 바꾸기
for i in range(N):
    ls =list(map(int,input().split()))
    for j in range(N):
        if ls[j]==1:
            graph[i].append(j)


visit = [[0]*N for _ in range(N)]   # a->b로 가는 길의 유무
def dfs(start):                     # 시작값 start
    global root                     # root는 한 줄 씩 만들어 진다고 보면 됨
                                    # root번째 줄의 visit를 만드는 과정
    for i in graph[start]:          # start에서 나오는 길 중에
        if visit[root][i]==0:       # root-> i 가 아직 안갔으면
            visit[root][i]=1        # 방문처리하고 , i->다른거로 가는 길 찾기
            dfs(i)



for root in range(N):       # N까지 한 줄 씩 visit를 만드는 과정
    dfs(root)

for v in visit:
    print(*v)

