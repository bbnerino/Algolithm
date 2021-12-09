n= int(input())
paper = [[0]*101 for _ in range(101)]
# 빈 격자판
for i in range(1,n+1):
    x,y,w,h =map(int,input().split())
    for j in range(x,x+w):
        for k in range(y,y+h):
            paper[j][k]+= i

for i in range(1,n+1):
    count=0
    for m in paper:
        count += m.count(i)
    print(count)