a= int(input())
b= list(map(int,input().split()))   
result = 100
for i in b:
    if i<=result:
        result=i
print(result)