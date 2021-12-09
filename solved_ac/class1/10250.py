t = int(input())
for i in range(t):
    h,w,n = map(int,input().split())
     # 4 , 12
    if n%h==0:
        x=h
        y=n//h
    else:
        x=n%h
        y= n//h +1 # 2 3
    if y<10:
        print(f"{x}0{y}")
    else:
        print(f"{x}{y}")