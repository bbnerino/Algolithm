import sys
sys.stdin = open('input.txt')
import heapq


# 소수 찾기
prime = [True]*10000    # 10000까지의 수중에
for i in range(0,1000): # 네자리 미만은 소수가 아니다 표시
    prime[i]=False

for i in range(2,10001):    # 2부터 10000까지 돌면서
    for j in range(2,9999//i+1): # 10000까지의 i의 배수들을(2부터시작)
        prime[i*j]= False       # 소수 탈락시킨다.


def bfs(a,b):           # 시작점 끝점이 들어온다.
    visited = [10000]*10000 # 최소거리를 찾기 위한 visited (큰수)
    visited[a]= 0           # 시작점 0
    Q = []
    heapq.heappush(Q,[0,a])

    while Q :
        count,a = heapq.heappop(Q)  # 바뀐횟수, 현재 숫자 를 pop
        intA = list(str(a))         # 현재 숫자를 문자열화 해준다.

        if a==b:                    # a==b 같으면 끝낸다
            print(count)
            return

        for i in range(4):          # 네자리를 돌면서 [a b c d]
            for j in range(10):     # 그 숫자들을 0~9 까지의 숫자들로 바꿔준다.
                this=""             # 빈 문자열을 만들고
                for k in range(4):  # a의 자리를 하나씩 추가해주는데 i번째 숫자는 j로 바꿔준다.
                    if k ==i :
                        this+= str(j)
                    else:
                        this+= intA[k]

                if prime[int(this)] and count<visited[int(this)]:   # 이 숫자가 소수이면서 현재 count 보다 작다면
                    visited[int(this)]=count                        # 방문해주고 , Q에 넣어준다.
                    heapq.heappush(Q,[count+1,int(this)])


tc = int(input())
for _ in range(tc):
    a,b = map(int,input().split())
    bfs(a,b)
