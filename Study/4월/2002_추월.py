import sys
sys.stdin = open('input.txt')

N = int(input())
graph1,graph2 = [] ,[]

for _ in range(N):  # 인풋값
    graph1.append(input())
for _ in range(N):  # 결과값
    graph2.append(input())

count = 0  # 추월한 횟수
# 인풋 : A B C D E
# 결과 : B E D A C
# 결과값을 맨 앞부터 하나씩 확인해서 그 값이  그 index에 없으면
# 그 index에 원래 있던 위치에서 가져와 넣어주고 count를 추가해줍니다
# A B C D E => B A C D E => B E A C D => B E D A C
#               +1           +1           +1

for i in range(N):   # 결과값을 하나씩 확인을 합니다 .
    now = graph2[i]
    if graph1[i] != now:
        graph1.insert(i, graph1.pop(graph1.index(now)) )
        count+=1
print(count)

