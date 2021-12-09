numlist= [] # 3 ~ 7  더하기
for i in range(50):
    n=i
    while n !=0 :
        numlist.append(i)
        n-=1
a,b = map(int,input().split())
sum = 0
for i in range(a-1,b):
    sum += numlist[i]
print(sum)
