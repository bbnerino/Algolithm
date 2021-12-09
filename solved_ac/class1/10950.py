T = int(input())
xlist = []
ylist = []
for i in range(T):
    x,y = input().split()
    xlist += x
    ylist += y
for k in range(T):
    print(int(xlist[k])+int(ylist[k]))
