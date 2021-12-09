import sys
sys.stdin = open('input.txt')
from collections import deque 

N, M, R = map(int,input().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

result=[[0 for _ in range(M)] for _ in range(N)] # 결과값을 먼저 만들어줌

# turn(0,0,N,M)  - 시작점 , 끝점
def turn(fy,fx,ly,lx):    # 회전하기 함수
    index = [fy, fx]    # 현재 index 위치
    start=[fy,fx]       # 시작점 0,0  -> 1,1
    end = [ly,lx]         # 끝점 4,4    -> 3,3

    num_index = deque() # 숫자의 위치와 위치의 내용을 받아옴
    num_list = deque()  # 큐를 이용해 순회하는 숫자들을 리스트 내에서 돌려줄 예정

    dy = [0, 1, 0, -1]       # 우 -> 하 -> 좌 -> 상
    dx = [1, 0, -1, 0]       # 순으로 돌고
    d = 0                    # d= 0번부터

    while d<4:               # 3번까지만 돌면 끝 라인 전부 순회가능
        ny = index[0]+dy[d]
        nx = index[1]+dx[d]  # 찾을 위치

        if start[0] <= ny < end[0] and start[1] <= nx < end[1]: # 범위내에 있을때,
            num_index.append([ny, nx])      # 맨 끝 숫자들의 인덱스와 
            num_list.append(graph[ny][nx])  # 그 값을 큐에 넣어둔다
            index = [ny, nx]                # 현재 위치를 옮긴다
        else:    # 범위내에 있지않다 -> 그래프를 넘으면
            d += 1  # 방향을 바꾼다
            
    if len(num_list) == 0:            # 홀수열 일때,  3행 3열 행렬일 경우 중간의 값이 안들어감
        num_index.append([fy, fx])    # 첫값 -> graph[2][2] 값을 추가
        num_list.append(graph[fy][fx])
    
    for _ in range(R % len(num_list)):  # R의 값이 엄청 크다 -> 회전을 해봤자 돌아온다
                                        # 나머지 값을 이용해 값을 줄여준 상태로
        num_list.append(num_list.popleft())     # 맨앞의 값을 빼서 맨 뒤로 넣어준다

    for i in range(len(num_index)): # num_index값은 차례대로 [0,1],[0,2].. 그대로 이므로
                                    # 바뀐 num_list를 그 위치에 넣어주면 된다
        result[num_index[i][0]][num_index[i][1]] = num_list[i]

    for r in result:                            # 결과값에서
        if 0 in r:                              # 아직도 0인 값이 있다면
            return turn(fy+1, fx+1, ly-1, lx-1) # 한칸 안으로 들어가서 다시 turn함수 실행

turn(0,0,N,M)
for r in result:
    print(*r)

