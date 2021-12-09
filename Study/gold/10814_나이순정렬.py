
n=int(input())
result=[]
for i in range(n):
    age,name=input().split()
    age=int(age)
    result.append((age,name))
result = sorted(result,key=lambda x:x[0])

for i in result:
    print(i[0],end=" ")
    print(i[1])