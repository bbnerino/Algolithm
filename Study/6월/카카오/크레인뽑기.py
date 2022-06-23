board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

answer = 0
change = False
length = len(board[0])


def sortboard(board):
    change = False
    for one_line in board:
        while True:  # 0의 위치 이동시키기
            if 0 in one_line:
                one_line.remove(0)
            else:
                break
        while len(one_line) < length:
            one_line.insert(0, 0)

    for i in range(length):
        for j in range(length):
            if board[i][j]!=0:
                if check(i,j):
                    change = True
def check(y,x):
    global answer
    flag = False
    if y+1<length:
        if board[y][x] == board[y+1][x]:
            board[y][x] = 0
            board[y+1][x] = 0
            answer +=2
        flag = True
    if x+1<length:
        if board[y][x] == board[y][x+1] !=0 :
            board[y][x]=0
            board[y][x+1] = 0
            answer += 2
        flag = True
    return  flag

def crain(board,moves):
    global answer

    Q = []
    for move in moves:
        line = board[move-1]
        for i in range(length):
            if line[i] >0:
                board[move-1][i] = 0
                Q.append(line[i])
                if len(Q)>1:
                    if Q[-1]== Q[-2]:
                        Q = Q[0:-2]
                        answer+=2


def solution(board, moves):
    sortboard(board)
    if not change:
        crain(board,moves)
        return answer
    else:
        sortboard(board)
print(solution(board,moves))