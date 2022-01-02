import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
tree_for_leaf = [[]for _ in range(N+1)]
tree = [[]for _ in range(N+1)]

for _ in range(N-1):
    s,e,d = map(int,input().split())
    tree_for_leaf[s].append([e,d])

    tree[s].append([e,d])
    tree[e].append([s,d])


def dfs_leaf(n):        # 리프노드 구하기
    if tree_for_leaf[n]:
        for e,d in tree_for_leaf[n]:
            dfs_leaf(e)
    else:
        leaf.append(n)

# 리프노드 구하기
leaf = []
dfs_leaf(1)
# print(leaf)
# [7, 8, 9, 10, 11, 12]

result=[]
def dfs(cnt,n):
    visit[n]=1
    flag =False
    for e,d in tree[n]:
        if visit[e] ==0:
            dfs(cnt+d,e)
            flag =True
    if flag==False:
        result.append(cnt)

while leaf:
    start = leaf.pop()
    visit = [0] * (N + 1)
    dfs(0,start)
print(max(result))