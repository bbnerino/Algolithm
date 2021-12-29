import sys
sys.stdin = open('input.txt')

N = int(input())
row =[0]*N  # i번째 행에 든 위치
result =0   # 결과

def check(n):   # 유효성 검사
    for i in range(n):  # 끝까지 다할 필요없고 n까지만 하면된다.
                        # n번째 들어간 숫자가 이미 들어가 있는 숫자다?
                        # 행끼리의 차이 == 열끼리의 차이가 같으면 대각선에 있다
        if row[n]==row[i] or abs(row[i]-row[n])==n-i:
            return False
    return True

def dfs(n): # dfs를 이용해 들어간다
    global result
    if n==N:    # n이 하나씩 올라가서 N과 같아지면
        result +=1  # 결과 +1
        return

    for i in range(N): # n번째 줄에 들어갈 숫자를 0~N까지 다 넣어 본다
        row[n]= i
        if check(n):   # 그 숫자가 유효성 검사를 통과하면?
            dfs(n+1)   # dfs가 하나 늘어난다.


dfs(0)
print(result)