import sys
sys.stdin = open('input.txt')

H,W = map(int,input().split())
original_graph = list(map(int,input().split()))
graph = original_graph[::]
# 5 2 4 1 3 5 3 4


i = 0
big = i # 왼쪽부터 시작하는데 큰값을 자기로 잡고
while i<W: # 오른쪽에 위치한 값중 나보다 큰 곳 & 같은 곳이 있다면
    if graph[i]>= graph[big]:
        for j in range(big,i):  # 그 사이의 값을 모두 큰 값으로 바꿔준다
            graph[j] = graph[big]
        big = i                 # 이제 큰 값을 그 뒤부터가 된다.
    i += 1


k = W-1     # 뒤에서부터 시작하겠다
big2 = k
while k>=big:
    if graph[k]>= graph[big2]:  # 똑같이 왼쪽의 값이 큰 값보다 크거나 같다면
        for j in range(big2,k,-1):      # 바꿔준다.
            graph[j] = graph[big2]
        big2 = k
    k -= 1

result =0
for i in range(W):      # 바꿔준 값들의 차이가 빗물양
    result += graph[i]-original_graph[i]
print(result)

