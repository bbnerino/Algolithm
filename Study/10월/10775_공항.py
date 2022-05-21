import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
G = int(input())
P = int(input())




count=0
visit = [0]*(G+1)
for _ in range(P):
    plane=int(input())
    flag = 0

    for i in range(plane,0,-1):
        if visit[i]==0:
            flag=1
            visit[i]=1
            count+=1
            break

    if flag==0:
        print(count)
        break


