N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

# 삼각형 합 (현재index, 몇쨋줄 , 합)
def triangleSum(graph):
    idx=1
    while idx <N:
        line = graph[idx]
        for i in range(len(line)):
            if i==0:
                line[i] = graph[idx-1][i] + line[i]
            
            elif 0<i<len(line)-1:
                line[i] = max(graph[idx-1][i]+ line[i], graph[idx-1][i-1]+line[i])
            else:
                line[i]= graph[idx-1][i-1] + line[i]    
        idx+=1
    return graph[idx-1]

print(max(triangleSum(graph)))