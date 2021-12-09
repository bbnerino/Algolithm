n= int(input())
for i in range(19):
    x,y =input().split()
    for j in range(1,20):
        if i[j][int(y)]==0:
            i[j][int(y)] =1
        else:
            i[j][int(y)]=1
        if i[int(x)][j]==0:
            i[int(x)][j]=1
        else:
            i[int(x)][j]=0

