import sys
sys.stdin = open('input.txt')
import heapq
# 이미 한개를 입력했다
# 1.모두 복사 => 클립보드 저장
# 2.클립보드 => 화면 붙여넣기
# 3.화면에 있는 임티 한개 삭제

s = int(input())
def bfs():
    Q = []
    heapq.heappush(Q,[1,1,1])
    visit = [False]*1001
    visit[1] = True
    while Q:
        count,number,clipboard = heapq.heappop(Q)
        if number == s:
            print(count)
            quit()
        if number>0:
            try:
                visit[number] = True
            except:
                pass
            if number!=clipboard : # 클립보드가 그 전이랑 다르다면?
                Q.append([count+1,number,number]) # 클립보드에 복사하기
            if number+clipboard<1001 and not visit[number+clipboard]:
                Q.append([count+1,number+clipboard,clipboard])
            if not visit[number-1]:
                Q.append([count+1,number-1,clipboard])

bfs()
