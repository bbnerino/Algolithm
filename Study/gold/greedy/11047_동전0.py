N,K= map(int,input().split())
coin=[]
for n in range(N):
    coin.append(int(input())) # 숫자들 N개 입력 받음
# [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
count = 0 # 숫자를 센다
for i in range(len(coin)-1,-1,-1): # 9~0 까지 // 큰 값부터 계산하겠다
    count += K//coin[i] # 4200 원 // 1000원 -> count+4 
    K-= (K//coin[i]) * coin[i] # 4200 - 4*1000
print(count)