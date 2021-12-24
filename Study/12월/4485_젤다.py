import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

import heapq
def bfs():
    Q = []
    heapq.heappush(Q,[cave[0][0],0,0])
    visited = [[1e9]*N for _ in range(N)]   # 다익스트라 스킬 ( 큰 수로 미리 지정을 해준 다음)
    visited[0][0] = cave[0][0]  # 첫값은 넣어주고 지나가는 길마다 더해줄 예정인데, 그 값이
                                # visited에 있는 값보다 작으면 바꿔준다.
    while Q:
        money, y, x = heapq.heappop(Q)
        if y==N-1 and x==N-1:
            print('Problem {}: {}'.format(Tc,money))
        dy= [1,-1,0,0]
        dx =[0,0,1,-1]
        for i in range(4): # 네방향 순회하면서
            ny = dy[i]+y
            nx = dx[i]+x
            if 0<=ny<N and 0<=nx<N:
                if visited[ny][nx] > money + cave[ny][nx]: # 다음값과 지금 들고있는 값의 합이
                                                        # visited보다 크면 볼 필요없고
                                                        # ''보다 적으면 visited 바꿔주고 Q에 넣기
                    next_money = money + cave[ny][nx]
                    visited[ny][nx] = next_money
                    heapq.heappush(Q,[next_money,ny,nx])



Tc = 0
while True:
    Tc += 1
    N = int(input())
    if N:
        cave = []
        for _ in range(N):
            cave.append(list(map(int,input().split())))
        bfs()

    else:
        break

