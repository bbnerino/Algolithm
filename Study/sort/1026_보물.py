N = int(input())

Alist = list(map(int,input().split()))
Blist = list(map(int,input().split()))
Alist.sort()
Blist.sort(reverse=True)
result=0
for i in range(N):
    result += Alist[i]*Blist[i]
print(result)
