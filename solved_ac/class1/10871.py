x,y = map(int,input().split())
a = list(map(int,input().split()))
for i in range(len(a)):
    if a[i] < y :
        print(a[i],end=" ")
