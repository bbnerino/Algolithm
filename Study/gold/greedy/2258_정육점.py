N,M= map(int,input().split())
meat=[]
for ts in range(N):
    kg,won = map(int,input().split())
    meat.append([kg,won])
# 0 무게 1 가격
meat = sorted(meat, key = lambda x : (x[1],-x[0]))

total=0
money =0
for i in range(len(meat)):
    total += meat[i][0]
    if i > 0 and meat[i][1] == meat[i - 1][1]:
        money += meat[i - 1][1]
    else:
        money = 0
    if total >= M:
        check = meat[i][1]
        result = meat[i]
        index = i
        money += meat[i][1]
        result[1] = money
        break
    else:
        result =[0, -1]

if result[1] != -1:
    for i in range(index+1, N):
        if result[1] >= meat[i][1] and check != meat[i][1] :
            result = meat[i]

print(result[1])
