import sys
sys.stdin = open('input.txt')

N,d,k,c = map(int,input().split())

# N 초밥개수 d : 의미x  k:연속 초밥 , c : 쿠폰번호

graph =[]
for _ in range(N):
    graph.append(int(input()))

graph.extend(graph[0:k])
# 회전판이기 때문에 연속으로 뽑는 초밥수만큼 처음의 초밥들을 더해줍니다.

result = 0 # 최대초밥수
for i in range(N):
    newgraph =graph[i:i+k] # 1~4, 2~5,3~6... 모든 조합을 보는데
    if c not in newgraph: # 그 초밥안에 쿠폰초밥이 없다면
        newgraph.append(c) # 더해줍니다
    newgraph = list(set(newgraph)) # 먹은 초밥중 중복방지용
    result = max(result,len(newgraph)) # 가장 많은 초밥수를 구합니다
print(result)