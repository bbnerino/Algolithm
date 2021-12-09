
a= input().split("-")
for i in range(len(a)):
    a[i]= a[i].split("+")

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j]=int(a[i][j])

result = sum(a[0]) 
for i in range(1,len(a)):
    result-= sum(a[i])
print(result)