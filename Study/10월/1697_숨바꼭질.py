N, K = map(int, input().split())


def bfs(num, target):
    global Q
    Q = [[num, 0]]          # 숫자,count를 넣는다
    visit = [0] * 1000000   # 갔던 숫자는 다시 가지 않게끔 만들어준다
    while True:             # 반복용
        s = Q.pop(0)
        if s[0] == target:  # 타겟숫자라면
            print(s[1])     # count 출력
            break
        try:                            # index 에러를 막기위해 try
            if visit[s[0] + 1] == 0:    # 방문을 안했다면
                Q.append([s[0] + 1, s[1] + 1])  # 추가해준다
                visit[s[0] + 1] = 1
            if visit[s[0] - 1] == 0:
                Q.append([s[0] - 1, s[1] + 1])
                visit[s[0] - 1] = 1
            if visit[s[0] * 2] == 0:
                Q.append([s[0] * 2, s[1] + 1])
                visit[s[0] * 2] = 1
        except:
            pass



bfs(N, K)

