N= int(input())
seat= input()
L_count=0
S_count=0

for S_L in seat:
    if S_L =="S":
        S_count+=1
    else:
        L_count+= 0.5

# S가 나오면 왼쪽 하나 
# LL이 나오면 왼쪽 하나
# 마지막 +1개
# *S * LL * S * LL *
result= S_count + L_count + 1

if result > N:
    result = N

print(int(result))

    