N = int(input())
def jegop(N):
    dp = [0 for _ in range(N + 1)]
    special = [] # 1, 4, 9 16 .. 제곱수들을 저장해준다
    dp[1] = 1
    for i in range(1,N+1):
        if (i**(1/2)).is_integer():
            special.append(i)   # 제곱수들 추가
            dp[i] = 1           # 제곱수들은 1로 저장된다.

        else:
            result =[]        # 확인할 리스트
            for s in special: # 제곱수들을
                j = i - s     # i에서 뺀 값을 j에 저장
                result.append(dp[j] + 1) # result에는 [i에서 제곱수뺀 값들]의 dp값이 저장됨
            dp[i]=min(result) # 최소값찾기
    print(dp[N])

jegop(N)