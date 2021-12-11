import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N,M = map(int,input().split())

ladders = []
for _ in range(N+M):
    x,y = map(int,input().split()) # x번 칸에 도착하면, y번 칸으로 이동
    ladders.append([x,y])

import heapq
def bfs():
    Q = []
    heapq.heappush(Q,[0,1]) # count,  현재위치
    visit = [0]*100 # 방문등록을 함으로써, 중복 제거용
    visit[1]= 1
    while Q:
        count,now = heapq.heappop(Q) # count가 작은 순으로 처리하면 최단시간에 구해질 예정
        here= now   # 나중에 now값의 재사용을 위해

        for i in range(1,7): # 주사위 (1~6)까지 굴려서
            now += i    #  현재위치 =  전 위치 + 주사위 눈금

            if now == 100:     # 현재위치가 100 이되면
                print(count+1) # count 출력해주고
                return         # 함수를 끝낸다

            if now>100:        # 100을 넘어가게 되면
                break          # 멈추기

            for ladder in ladders:   # ladders에 맞는 자리가 있는지 확인
                if now == ladder[0]: # 있다면
                    now = ladder[1]  # 현재위치를 이동시킨다

            if visit[now]==0:        # 방문을 안했다면
                visit[now]=1         # 방문 시키고
                heapq.heappush(Q,[count+1,now]) # heap으로 count+1과 이동한 위치를 넣어준다
                                                # count가 작은 값이 맨 앞으로 이동된다
                now= here                       # now에 이동한 위치가 있는데
                                                # 다음 주사위 값을 위해 now를 주사위 눈금 더하기 전 값으로 바꿔준다

bfs()