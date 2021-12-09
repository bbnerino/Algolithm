N= int(input())
# 도시 개수
road = list(map(int,input().split()))
# 도로 길이
oil =list(map(int,input().split()))
# 주유 가격
total = 0
# 비용
length= 0
small=oil[0]
for i in range(len(road)):
    length+=road[i]    # 0 1 2 에서
    if small > oil[i+1]:
        total+= length*small
        small=oil[i+1]
        length=0
total+= small *length
print(total)
