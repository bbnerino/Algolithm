N,k= map(int,input().split())
human = list(range(1,N+1))
i=k # 3
result=[]
while human:
    try:
        if i > len(human):
            i -= len(human)
        result.append(human.pop(i-1)) # 2
        i += (k-1) # 2,4,6

    except:
        i -=len(human)


print("<"+", ".join(map(str,result))+">")