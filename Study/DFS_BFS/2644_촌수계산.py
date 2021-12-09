
N = int(input())
# N = 전체사람수
A,B = map(int,input().split())
# 촌수를 계산해야  하는 다른 두사람의 번호
m = int(input())
graph=[[]for _ in range(N+1)]
for ts in range(m):
    s,e = map(int,input().split())
    graph[e].append(s)
    graph[s].append(e)
# [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]

def bfs(A):
    global connect
    Q=[A]
    visit =[0 for _ in range(N+1)]
    connect = [0 for _ in range(N+1)]
    # 연결된 줄 개수 하나씩 늘리기 *중요*
    while Q:
        s = Q.pop(0)
        visit[s]=1
        for i in graph[s]:
            if visit[i]== 0:
                connect[i]=connect[s]+1
                # 연결이 될 때마다 s의 값에 1씩 추가 
                Q.append(i)

bfs(A)
# print(connect)
# [0, 2, 1, 3, 0, 0, 0, 0, 2, 2]
if connect[B]>0:
    print(connect[B])
else:
    print(-1)