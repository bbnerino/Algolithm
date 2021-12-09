result =[]
for ts in range(4):
    x1,y1,x2,y2,a1,a2,b1,b2 = map(int,input().split())
    big= max([x1,y1,x2,y2,a1,a2,b1,b2])
    paper = [[0]*(big+1) for _ in range(big+1)]
    
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            paper[i][j]+=1
    
    for i in range(a1,b1+1):
        for j  in range(a2,b2+1):
            paper[i][j]+=1

    total=0
    
    for i in range(big+1):
        for j in range(big+1):
            if paper[i][j]==2:
                total+=1
    if total==0:
        result.append("d")
    else:
        if x1== b1 or x2 == a1 :
            if total>1:
                result.append("b")
            elif total==1:
                result.append("c")
        else:
            result.append("a")

for i in range(4):
    print(result[i])