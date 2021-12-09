pibo = [[0,0] for _ in range(41)]
pibo[0]=[1,0] # 0 이 1번 
pibo[1]=[0,1] # 1이 한번 
for i in range(2,41): 
    pibo[i][0]= pibo[i-1][0]+pibo[i-2][0] # 0이 1번 1이 한번 
    pibo[i][1]= pibo[i-1][1]+pibo[i-2][1] # 거론되게 만든다.

# 1 0  
# 0 1
# 1 1
# 1 2
# 2 3
 # 공교롭게도 위 두개의 합이다
T = int(input())
result=[]
for ts in range(T):
    N= int(input())
    result.append(pibo[N])
for i in result:
    print(*i)