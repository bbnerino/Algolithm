import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq
N,K = map(int,input().split())

def bfs():
    result = []
    Q = []
    Q.append([0,N])

    visited = [False]* 10*K
    visited[N]=True
    minnum = 99999999
    while Q:
        count,now = heapq.heappop(Q)
        if count+1>minnum:
            break
        if 0<now*2<10*K:
            if now + 1 == K:
                result.append(count + 1)
                minnum = count + 1

            if  visited[now+1] == False :
                heapq.heappush(Q, [count + 1, now + 1])

            if now - 1 == K:
                result.append(count + 1)
                minnum = count + 1

            if visited[now-1] == False:
                heapq.heappush(Q,[count+1,now-1])

            if now * 2 == K:
                result.append(count + 1)
                minnum = count + 1

            if visited[now*2]== False:
                heapq.heappush(Q, [count + 1, now * 2])

            visited[now-1] = True
            visited[now+1] = True
            visited[now*2] = True

    print(result[0])
    print(len(result))

bfs()