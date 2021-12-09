N,K= map(int,input().split())
days=list(map(int,input().split()))

# 3 -2 -4 -9 0 3 7 13 8 -3
result=[]
big = sum(days[0:K]) # 1
total = sum(days[0:K]) # 0~5 까지 더해놓고
for i in range(len(days)-K):
    total = total - days[i] + days[i+K] # 맨앞 빼고 뒤에 하나 넣고 
    if total>big: # 이값이 큰거보다 크면 
        big=total # 값이다
print(big)
