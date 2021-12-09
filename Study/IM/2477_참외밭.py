N=int(input())
data=[]
big = [[]for _ in range(4)]
# 큰 값을 찾기위한 값
for i in range(6):
    direct, width =map(int,input().split())
    data.append([direct,width])
    big[direct-1].append(width)

square=data*2 # 두번 연달아 적음 ->> 
#  4 2 /3 1 3 1 /4 2 ... 3 1 3 1
# 연달아 4개 오는 중간값 두개가 작은 사각형
for i in range(6):
    if square[i][0]== square[i+2][0] and square[i+1][0]== square[i+3][0]:
        small = square[i+1][1]*square[i+2][1]


# direct 내용에 값이 하나면 큰 길이
large=1
for i in range(4):
    if len(big[i]) ==1:
        large*=big[i][0]
print(N*(large-small))


