T = int(input())
result=[]
for ts in range(T):
    N=(int(input()))
    if N>5:
        triangle=[0]*(N+1)
        triangle[1]=1
        triangle[2]=1
        triangle[3]=1
        triangle[4]=2
        triangle[5]=2
        for i in range(6,N+1):
            triangle[i]= triangle[i-1]+triangle[i-5]
        result.append(triangle[N])

    elif N==1 or N==2 or N==3:
        result.append(1)
    elif N==4 or N==5:
        result.append(2)

for i in result:
    print(i)