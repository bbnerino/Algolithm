a=int(input())
n=0
sum=0
while sum<a:
    sum+=n
    if sum<a:
        n+=1
if sum >=a:
    print(n)