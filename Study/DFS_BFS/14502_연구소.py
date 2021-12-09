from itertools import combinations
import sys
N,M = map(int,sys.stdin.readline().split())
graph =[]
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))

# 1,2 위치 세기
onecount=[]
twocount =[]
for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            onecount.append([i,j])
        if graph[i][j]==2:
            twocount.append([i,j])
# [[0, 1], [0, 2], [0, 3], [0, 6], [1, 0], [1, 1],...
# 3개를 조합을 해서 사용할 것
# -> from itertools import combinations
combin =list(combinations(onecount,3))

# [([0, 0], [0, 1], [0, 2]),    ([0, 0], [0, 1], [0, 3])....]

def bfs(a,b):
    Q = [[a,b]]
    visit =[] # 시간초과를 막기위해 만듬 ->  
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    while Q:
        s = Q.pop(0)
        newgraph[s[0]][s[1]] = 3
        for i in range(4):
            ny = s[0] + dy[i]
            nx = s[1] + dx[i]
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            if newgraph[ny][nx]==0:
                if [ny,nx] not in visit:
                    newgraph[s[0]][s[1]]=3
                    Q.append([ny,nx])
                    visit.append([ny,nx])

result =[]
for comb in combin:
    
    # newgraph= copy.deepcopy(graph)
    newgraph=[]
    for i in range(N):
        newgraph.append(graph[i][:])
    
    for i in range(3):
        newgraph[comb[i][0]][comb[i][1]]=1

    for i in twocount:
        bfs(i[0],i[1])

    count= sum(i.count(0) for i in newgraph)
    result.append(count)
    
print(result)
print(max(result))