
def sugar(n):
    result= n # 18
    for five_i in range(n//5+1): #다섯개짜리 4번
        for three_i in range(n//3+1): # 세개짜리 7번
            if 5*five_i+3*three_i == n: # 조합을 해서 n만들기
                result=min(result,five_i+three_i)
            else: # 안되면 패스
                pass
    if result==n:
        print(-1)
    else:
        print(result)

n=int(input())
sugar(n)

