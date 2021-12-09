a=1
while a:
    a,b,c = map(int,input().split())
    triangle = sorted([a,b,c])
    if a!=0:
        if triangle[0]**2 + triangle[1]**2 == triangle[2]**2:
            result ="right"
        else:
            result ="wrong"
    else:
        break
    print(result)
        
        
        
