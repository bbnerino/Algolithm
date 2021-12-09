N,K = map(int,input().split())
girl = [0 for _ in range(6)]
boy = [0 for _ in range(6)]
for i in range(N):
    sx,grade=map(int,input().split())
    if sx ==0:
        girl[grade-1]+=1
    else:
        boy[grade-1]+=1 
# [1, 2, 1, 0, 1, 1] 여 학년별로 숫자를 셈
# [2, 1, 3, 1, 2, 1] 남 
count=0
for i in range(6):
    if girl[i]%K==0: # 0명 2명 4명... 
        count+=girl[i]//K # 몫을 더해주면됨
    else:           
        count+=girl[i]//K+1 # 3명일때는 2방이 필요하니 +1


    if boy[i]%K==0:
        count+=boy[i]//K
    else:
        count+=boy[i]//K+1



print(count)