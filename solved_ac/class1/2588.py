a=int(input())
b=int(input())
c = b*1
while c>0:  
    print(a*(c%10))
    c = c//10
else:
    print(a*b)
        