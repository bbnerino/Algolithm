N = int(input())
s = [0 for _ in range(N)]
visit =[0]*N

def CrossCheck(x):  # 대각선 방향으로 겹치는 퀸이 있는지 확인
    for i in range(x):
        if abs(s[x]-s[i])==x-i:
            return False
    return True

def n_queen(x):
    global count

    if x == N:
        count+=1
        return

    for i in range(N):
        s[x] = i
        if CrossCheck(x):
            n_queen(x+1)

count =0
n_queen(0)
print(count)