import sys
sys.stdin= open('input.txt')
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def tree(start,end):
    if start>end:
        return
    div = end +1

    for i in range(start+1,end+1):
        if graph[start]< graph[i]:
            div = i
            break
    tree(start+1,div-1)
    tree(div,end)
    print(graph[start])


n= int(input())
graph=[]
count=0
while True:
    try:
        graph.append(int(input()))
        count+=1
    except:
        break

tree(0,len(graph)-1)