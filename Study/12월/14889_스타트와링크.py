import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from itertools import combinations


N = int(input())
nums = set(range(N)) # list가 아닌 set 사용 [1,2,3]-[1,2] ->[3] 용도
graph =[]   # 입력받기
for _ in range(N):
    graph.append(list(map(int,input().split())))

teams = list(combinations(nums,N//2)) # 두 팀으로 나누기 (모든 조합 찾기)
result = 9999999    # 임의의 큰수수

while teams:           # 모든 팀을 다 순회하면서
    start = list(teams.pop())       # 한 팀이 정해지면
    link = list(nums-set(start))    # 다른 한팀은 전체에서 위 팀을 뺀다

    startset = list(combinations(start,2)) #스타트팀에서 두명의 조합
    linkset = list(combinations(link,2))  # 링크팀에서 두명의 조합
    startRank = 0   # start 점수
    linkRank = 0   # link 점수
    for s in startset:  # 모든 두명의 조합의 합을 구해준다.
        startRank += graph[s[0]][s[1]]+graph[s[1]][s[0]]

    for l in linkset:
        linkRank += graph[l[0]][l[1]]+graph[l[1]][l[0]]

    result = min(result,abs(startRank-linkRank))  # 최소값 구하기
print(result)