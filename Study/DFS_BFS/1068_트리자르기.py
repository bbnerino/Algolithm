N= int(input())
parents = list(map(int,input().split()))
dlt = int(input())

leaf = list(range(N)) # 0,1,2,3,4 일단 모든값을 받고

son = [[] for _ in range(N)] 
for i in range(N):                      # 리프찾기
    if parents[i]!=-1:
        son[parents[i]].append(i) # 자식-> 부모를 ---> 부모-> 자식으로 바꿈
        if parents[i] in leaf:
            leaf.remove(parents[i]) # leaf안에 있다면 지워준다 ( 모든 부모들이 지워진다 )
# [[1, 2], [3, 4], [], [], []]

def bfs(num):
    global new_delete
    Q=[num]
    visit=[0 for _ in range(N)]
    new_delete=[num] # 리프에서 지울 것을 만들어준다
    
    while Q:
        s = Q.pop(0)
        visit[s]=1
        if len(son[parents[s]])==1: # 만약 tree(찾을값의 부모)의 자식이 하나라면
            leaf.append(parents[s]) # 부모의 값을 leaf에 추가
        for i in son[s]:            # 자식의 값이
            if visit[i]== 0:        # 방문안했을때
                Q.append(i)         # 큐 추가 하면서
                if i in leaf:
                    leaf.remove(i)
                new_delete.append(i)# 지울 값에 추가
                
bfs(dlt)
for i in new_delete:
    if i in leaf:
        leaf.remove(i)
print(len(leaf))

