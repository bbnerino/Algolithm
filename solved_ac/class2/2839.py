def sugar(n):
    result= n
    for five_i in range(n//5+1):
        for three_i in range(n//3+1):
            if 5*five_i+3*three_i == n:
                result=min(result,five_i+three_i)
            else:
                pass
    if result==n:
        print(-1)
    else:
        print(result)





n=int(input())
sugar(n)

