N = int(input())
choo = list(map(int, input().split()))
# [1, 1, 2, 3, 6, 7, 30]
choo.sort()

if choo[0]!=1: # 0번이 1이 아니면 
    result=1 # 1

elif choo[1] > 2: # 1번이 1,2 가 아니면 
    # result = choo[1] - 1 # 
    result = choo[0] + 1 # 2가 안나옴

else:
    for i in range(2, N): # 2번부터 ~ 
        front = sum(choo[0:i]) # i번 전까지의 합
        if front + 1 < choo[i]:  # i값이 저거보다 2 이상 크면
            result = front + 1  # 전까지의 합 +1 값이 안나옴
            break

        result = sum(choo) + 1
print(result)