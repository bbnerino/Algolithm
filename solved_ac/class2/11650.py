n=int(input())
result=[]
for i in range(n):
    x,y=map(int,input().split())
    result.append([x,y])

result.sort(key=lambda z: (z[0],z[1]))
# 두가지 연달아 정렬하기!


for i in result:
    print(i[0],i[1])

