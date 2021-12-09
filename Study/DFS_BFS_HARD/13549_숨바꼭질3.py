import sys
sys.stdin =open('input.txt')


import heapq
def hide(start,target):

    # if start>target:
    #     return start-target

    visit = [-1]*1000001
    visit[start] = 0
    Q = []
    heapq.heappush(Q,[0,start])
    while Q:
        count,s = heapq.heappop(Q)
        if s == target:                     # 타겟찾으면
            return visit[s]                 # 출력한다
                                            # 순서가 이렇게 중요하다고? 와..

        if 0<=s*2<=1000000:                 # 범위 내에 있고
            if visit[s*2]==-1:              # 아직 방문을 안했다면
                visit[s*2]= visit[s]        # 방문을 시켜준다 순간이동일 경우 그 전 값 그대로
                heapq.heappush(Q,[count,s*2])   # count랑 같이 넣어주게 된다면 작은 순서대로
                                                # deque를 사용하게 된다면 appendleft 사용하면 됨
        if 0<= s-1 <=1000000:
            if visit[s-1]==-1:
                visit[s-1]= visit[s]+1
                heapq.heappush(Q,[count+1,s-1])

        if 0<=s+1<=1000000:
            if visit[s+1]==-1:
                visit[s+1]= visit[s]+1
                heapq.heappush(Q,[count+1,s+1])


N,K = map(int,input().split())

print(hide(N,K))

