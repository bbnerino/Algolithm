a= int(input())
b = list(map(str,input().split())) 
#[1, 3, 2, 2, 5, 6, 7, 4, 5, 9]
for i in range(1,24):
    i = str(i)
    print(b.count(i),end=" ")