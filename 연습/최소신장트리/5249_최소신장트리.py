import sys
sys.stdin = open('input.txt')


def find_parent(parent,x):
    # 루트노드가 나올 때 까지 재귀로 호출
    if parent[x] !=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b) # 루트부모노드 저장
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


T = int(input())
for tc in range(T):
    V,E = map(int,input().split())  # V = 노드개수 , E = 간선개수
    graph = []
    parent =[0]*(V+1)
    result = 0

    for i in range(1,V+1):
        parent[i]=i

    for _ in range(E):
        a,b,w = map(int,input().split())
        graph.append([w,a,b])
    graph.sort()
    for g in graph:
        dis,a,b = g
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            result += dis
    print("#{} {}".format(tc+1,result))
