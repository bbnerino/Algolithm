n,k=map(int,input().split())
money=[]
for i in range(n):
    money.append(int(input()))
# [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
result=0
while k :
    for i in range(len(money)-1,-1,-1):
        if k//money[i]!=0:
            result += k//money[i]
            k=k-(money[i]*(k//money[i]))
print(result)



