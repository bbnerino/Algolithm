width,height=map(int,input().split())
T=int(input())
x=[0,width]
y=[0,height]
for ts in range(T):
    type, cut = map(int,input().split())
    if type==0:
        y.append(cut) # [0, 8, 3, 2]
    else:
        x.append(cut) # [0, 10, 4]
x.sort()
y.sort()

bigx=0
for i in range(len(x)-1):
    if x[i+1]- x[i] >bigx:
        bigx = x[i+1]- x[i]
bigy=0
for i in range(len(y)-1):
    if y[i+1]- y[i] >bigy:
        bigy = y[i+1]- y[i]
print(bigx*bigy)