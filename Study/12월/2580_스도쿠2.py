import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

graph = [list(map(int,input().split())) for _ in range(9)]

zeros =[]                   # 0 위치 찾아주기
for i in range(9):
    for j in range(9):
        if graph[i][j]==0:
            zeros.append([i,j])

def no_numbers(i,j):    # 가로, 세로, 사각형에서 없는 숫자 찾기
    nums = list(range(1,10))   #1~9까지의 수 중에

    for k in range(9):
        if graph[i][k] in nums:     # 가로에서 없는수 찾기
            nums.remove(graph[i][k])

        if graph[k][j] in nums:     # 세로에서 없는 수 찾기
            nums.remove(graph[k][j])

    i//=3
    j//=3
    for p in range(i*3,(i+1)*3):    # 정사각형에서
        for q in range(j*3,(j+1)*3):
            if graph[p][q] in nums: # 없는수 찾기
                nums.remove(graph[p][q])
    return nums         # 1~ 9 중에 없는 숫자를 돌려준다

finish = False      # 출력 한번 하면 끝나는 조건

def dfs(x):         # x가 0의 위치 index 0번부터 마지막 index까지 채워지면 끝나는 것
    global finish
    if finish:      # 끝났다면
        return      # 함수끝내기

    if len(zeros) == x:                # x가 증가해서 zero 갯수만큼 채워지게 된다면
        for i in graph:                # 출력하고 끝내준다.
            print(*i)
        finish = True                  # 끝났다 확인해주기
        return


    i,j = zeros[x]
    nums = no_numbers(i,j) # [1~9] 까지중 없는 숫자 전부
                            # 만일 nums가 비어있다면 ?
                            # dfs가 깊어지지 않고 돌아간다 -> x 가 작아진다.
    for num in nums:             # 그 숫자들을 하나씩 넣는다
        graph[i][j]= num          # 바꿔주고
        dfs(x+1)                  # 다시 다음 숫자로 가기 (x+1)
        graph[i][j]=0              # 원래대로 고치기
dfs(0)