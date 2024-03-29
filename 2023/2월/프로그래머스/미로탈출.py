maps = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]

import heapq
def solution(maps):
    INF = 100000000
    graph = []
    START_POINT = [0,0]
    END_POINT  = [0,0]
    LEVER_POINT = [0,0]
    for i in range(len(maps)):
        tmp = []
        for j in range(len(maps[i])):
            if maps[i][j]=="S":
                START_POINT = [i,j]
                tmp.append(0)

            elif maps[i][j]=="E":
                END_POINT = [i,j]
                tmp.append(INF)

            elif maps[i][j]=="L":
                LEVER_POINT = [i,j]
                tmp.append(INF)
            
            elif maps[i][j]=="O":
                tmp.append(INF)
            
            elif maps[i][j]=="X":
                tmp.append("X")

        graph.append(tmp)

    def dijkstra(goal,start):
        Q = []
        heapq.heappush(Q,[start[0],start[1],start[2]])
        dy = [0,0,1,-1]
        dx = [1,-1,0,0]
        while Q: 
            count,y,x = heapq.heappop(Q)
            for i in range(4):
                ny = dy[i]+ y
                nx = dx[i]+ x
                if 0<=ny<len(graph) and 0<=nx<len(graph[0]):
                    if ny==goal[0] and nx==goal[1]:
                        return (count+1)
                    if type(graph[ny][nx])==int:
                        if graph[ny][nx] > count+1:
                            graph[ny][nx] = count+1
                            heapq.heappush(Q,[count+1,ny,nx])
        return (-1)
    
    def reset(y,x,count):
      for i in range(len(graph)):
          for j in range(len(graph[0])):
              if i==y and j== x :
                  graph[i][j] = count
              else:
                  if type(graph[i][j])==int:
                      graph[i][j] = INF

    Lcount= dijkstra(LEVER_POINT,[0,START_POINT[0],START_POINT[1]])
    if Lcount==-1: 
        return -1
    
    reset(LEVER_POINT[0],LEVER_POINT[1],Lcount)
    result = dijkstra(LEVER_POINT,[Lcount,END_POINT[0],END_POINT[1]])
    
    return result

print(solution(maps))