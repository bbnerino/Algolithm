import sys
sys.stdin = open('input.txt')
T = int(input())
for ts in range(T):
    W, H = map(int, input().split())
    graph = []
    for _ in range(H):
        graph.append(list(map(int,input().split())))

    # 홀수일때 1번
    dy1 = [0,0,1,-1, 1, 1]
    dx1 = [1,-1,0,0, -1, 1]

    # 짝수일 때 2번
    dy2 = [0,0,1,-1, -1, -1]
    dx2 = [1,-1,0,0, -1, 1]


    def dfs(y, x, time, score, visited):
        # visited.append([y,x])
        if time != 4:  # 네개 안채웠을 때
            try:
                if len(visited) > 6:
                    scorelist.append(score)
            except:
                pass
            if x % 2 == 0:  # 짝수이면
                for i in range(6):
                    ny = dy2[i] + y
                    nx = dx2[i] + x
                    if 0 <= ny < H and 0 <= nx < W:
                        if [ny, nx] not in visited:
                            visited.append([ny, nx])
                            dfs(ny, nx, time + 1, score + graph[ny][nx], visited)
                        if [ny, nx] in visited:
                            if [ny, nx] == visited[-1]:
                                visited.append([ny, nx])

                                dfs(ny, nx, time, score, visited)
                    # if 0<=ny<H and 0<=nx<W and [ny,nx] == visited[-1]:
                    #     dfs(ny,nx,time,score,visited)

            if x % 2 == 1:
                for i in range(6):
                    ny = dy1[i] + y
                    nx = dx1[i] + x
                    if 0 <= ny < H and 0 <= nx < W and [ny, nx] not in visited:
                        visited.append([ny, nx])
                        dfs(ny, nx, time + 1, score + graph[ny][nx], visited)
                    if [ny, nx] in visited:
                        if [ny, nx] == visited[-1]:
                            visited.append([ny, nx])

                            dfs(ny, nx, time, score, visited)
                    # if 0<=ny<H and 0<=nx<W and [ny,nx] == visited[-1]:
                    #     dfs(ny,nx,time,score,visited)
        if time == 4:
            scorelist.append(score)


    scorelist = []
    visitedlist = []
    for i in range(H):
        for j in range(W):
            dfs(i, j, 1, graph[i][j], [[i, j]])

    print(f'#{ts+1} {max(scorelist)**2}')