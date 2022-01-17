import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N,R = map(int,input().split())
tree = [[] for _ in range(N+1)]    # 트리 입력받기
for _ in range(N-1):
    a,b,d = map(int,input().split())
    tree[a].append([b,d])

center = 1
for t in range(N+1):
    if len(tree[t])>1:
        center = t

leaf =[]
def LEAF(start):
    if tree[start]:
        for e,d in tree[start]:
            LEAF(e)
    else:
        leaf.append(start)
LEAF(center)
print(center)
print(leaf)


def ROOT(start):
    global root,giga
    root = 0        # 총 길이
    giga = start     # 마지막점 -> (시작점)
    while len(tree[giga])==1:
        e,d = tree[giga][0]
        root += d
        giga = e
ROOT(1)
print(root,end=" ")
# print(end)

result =[]
def dfs(start):
    global stick
    if len(tree[start])==0:
        result.append(stick)
    for e,d in tree[start]:
        stick+=d
        dfs(e)
        stick-=d

stick = 0
dfs(giga)
print(max(result))