N = int(input())  # 보드크기
K = int(input())  # 사과개수
graph = [[0 for _ in range(N)] for _ in range(N)] # 지도 그리기
for _ in range(K):
    y, x = map(int, input().split())
    graph[y - 1][x - 1] = 2  # 사과는 2로 바꿔줌

L = int(input())  # 방향 변환 횟수
change_time,change_vector = [],[] # 시간과 방향을 따로 만듬
for _ in range(L):
    X, C = map(str, input().split())
    change_time.append(int(X))
    change_vector.append(C)

snake = [[0, 0]] # 시작점 위치
dy = [0, 1, 0, -1] # 우 하 좌 상 
dx = [1, 0, -1, 0] # 으로 움직이게 한다
time = 0  # 지난 시간 
i = 0 # 시작 방향 => 오른쪽
graph[0][0] = 1 # 뱀이 있는 자리 = 1

while True: # break 될때까지 진행
    if time in change_time: # 시간이 changetime 에 있다면
        if change_vector[change_time.index(time)] == "L": # 벡터가 L인지 D인지 판단
            i -= 1 # 왼쪽 
        else:
            i += 1 # 오른쪽
        i = i % 4 # 0~3을 벗어나지 않게 다시 바꿔준다
    # snake = [tail body body body .... head]
    head = snake[-1]     # 머리를 먼저 확인
    ny = head[0] + dy[i] # 다음 진행방향 
    nx = head[1] + dx[i]
    time += 1 # 부딪히든 진행하든 시간은 간다.

    if ny < 0 or nx < 0 or ny >= N or nx >= N: # 벽이랑 만날때
        break
    if graph[ny][nx] == 1: # 자기랑 만남
        break
    elif graph[ny][nx] == 0: # 이동할 때, 
        tail = snake.pop(0)  # 꼬리가 빠지고
        graph[tail[0]][tail[1]] = 0 # 꼬리 삭제

        graph[ny][nx] = 1    # 머리가 이동된다
        snake.append([ny, nx]) # 머리 추가
        
    elif graph[ny][nx] == 2: # 사과가 있으면
        snake.append([ny, nx]) # 머리만 추가
        graph[ny][nx] = 1    # 머리추가
print(time)
