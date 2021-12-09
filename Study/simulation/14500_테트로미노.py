# import sys
# sys.stdin = open('input.txt')

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
# print(graph)
tetris_I = [ [[0,0],[0,1],[0,2],[0,3]] , [[0,0],[1,0],[2,0],[3,0]] ]
# 1자 2개
tetris_nemo = [ [[0,0],[0,1],[1,0],[1,1]] ]
# ㅁ자 1개
tetris_ah = [ [[0,0],[0,1],[0,2],[1,1]], [[1,0],[0,1],[1,1],[2,1]] ,[[0,0],[1,0],[2,0],[1,1]], [[0,1],[1,0],[1,1],[1,2]] ]
# ㅏ자 4개
tetris_Z = [[[0,0],[0,1],[1,1],[1,2]],[[1,0],[1,1],[0,1],[0,2]],[[0,1],[1,1],[1,0],[2,0]], [[0,0],[1,0],[1,1],[2,1]]]
# Z자 4개
tetris_L = [ [[0,0],[1,0],[2,0],[2,1]],[[0,0],[0,1],[1,1],[2,1]],[[1,0],[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2],[0,2]],
            [[0,1],[1,1],[2,1],[2,0]],[[0,1],[0,0],[1,0],[2,0]],[[0,0],[1,0],[1,1],[1,2]],[[0,0],[0,1],[0,2],[1,2]] ]
# L자 8개
every = tetris_ah + tetris_I + tetris_L + tetris_nemo + tetris_Z
result =[]



def find():
    while every:
        index = every.pop()
        # [[0,0],[0,1],[0,2],[0,3]]
        for i in range(N):
            for j in range(M): # 모든 값을 순회하면서
                total = 0 # 각각의 점수를 만든다
                for k in range(4): # 네자리를 다 확인해준다
                    ny = i+index[k][0] 
                    nx = j+index[k][1]
                    if 0 <= ny < N and 0 <= nx < M : # 범위내에 있으면
                        total += graph[ny][nx] # 점수에 추가
                    else: # 범위내에 없으면 
                        total =0 # 0점이 되고 
                        break  # i와 j를 바꾼다
                result.append(total)
find()
# print(result)
print(max(result))










