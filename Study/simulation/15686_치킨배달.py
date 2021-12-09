from itertools import combinations
N,M = map(int,input().split()) 
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

house,original_chicken=[],[] # 치킨집과 가정집을 입력받음
for i in range(N):
    for j in range(N):
        if graph[i][j]==2: # 2면 치킨
            original_chicken.append([i,j]) 
        elif graph[i][j]==1: # 1이면 가정집
            house.append([i,j])

combi = list(combinations(original_chicken,M)) # 치킨집의 조합을 리스트로 만들어놓는다

result = [] # 결과표
while combi: # 조합을 하나씩 꺼내서
    chicken = combi.pop() # 치킨집으로 남긴다
    delivery = [0 for _ in range(len(house))] # 집집마다의 거리를 저장
    for h in range(len(house)):
        for c in range(len(chicken)):
            if delivery[h]==0: # 아직 계산을 안했다면 거리 계산
                delivery[h]= abs(house[h][0]-chicken[c][0])+abs(house[h][1]-chicken[c][1])
            else:  # 이미 계산이 된 집이라면 최소값만 저장
                delivery[h] = min(delivery[h],abs(house[h][0]-chicken[c][0])+abs(house[h][1]-chicken[c][1]))
    result.append(sum(delivery)) # 집집마다의 거리를 다 더한게 결과값
# print(result)
print(min(result)) # 그중의 최소값을 찾음