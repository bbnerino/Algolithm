N,K,B = map(int,input().split())
traffic =[1]*(N+1)
traffic[0]=0
for _ in range(B):              # 신호등 끄기
    traffic[int(input())]=0


# 1 2 3 4 5 6 7 8 9 10
# X X O O X O O O X X
#|0 0 0 0 0 3|2 1 2 3
# 0|0 0 0 0 3 2|1 2 3
# 0 0|0 0 0 3 2 1|2 3   슬라이딩 윈도우

# [0, 0, 0, 1, 1, 0, 1,/ 1, 1, 0, 0]

check = [0]*(N+1)       # 새로운 리스트에 K개의 합을 추가해준다
check[K]= sum(traffic[1:K+1])
for i in range(K+1,N+1):    # 시간단축을 위해 앞에서 하나 빼고 뒤에 하나 추가를 해준다.
    check[i]=check[i-1]+traffic[i]-traffic[i-K]

# [0, 0, 0, 0, 0, 0, 3, 4, 5, 4, 3]
print(K-max(check))


