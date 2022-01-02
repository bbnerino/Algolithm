import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
tree = [[]for _ in range(N+1)]

for _ in range(N-1):
    s,e,d = map(int,input().split())
    tree[s].append([e,d])   # 트리 양방향성
    tree[e].append([s,d])


length = 0      # 제일 긴길이 찾기
startpoint = 0  # 제일 긴길이의 노드번호

def dfs(cnt,n):
    global length,startpoint
    visit[n]=1  # 방문을 해주고

    flag= True  # 이 노드에서 더이상 들어갈 곳이 없다 =True
    for e,d in tree[n]: # start-> end (distance)
        if visit[e]==0: # end 지점이 방문을 안햇으면
            dfs(cnt+d,e) # 들어가준다
            flag=False   # 더 들어갔다 체크

    if flag==True:      # 더이상 들어갈 곳이 없다면
        if length<=cnt: # 가장 긴 길이가 맞는지 확인하고
            length=cnt  # 바꿔준다
            startpoint = n  # 시작지점도 바꿔준다

visit=[0]*(N+1)     # 방문 체크용
dfs(0,1) # 1에서 가장 먼곳 찾는 dfs

visit=[0]*(N+1) # 방문체크 초기화
dfs(0,startpoint)   # 찾은 노드에서 새롭게 찾기
print(length)   # 가장 긴 길이 출력
