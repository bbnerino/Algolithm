a,m,d,n= map(int,input().split()) 
# 1 -2 1 8

result = a
for i in range(n-1):
    result = result*m +d
print(result)