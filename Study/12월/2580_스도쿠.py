import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

graph = []
xgraph = [0]*9 # [9, 2, 2, 1, 2, 1, 2, 2, 1]
ygraph = [0]*9 # [2, 3, 2, 2, 3, 2, 2, 3, 3]

for _ in range(9):
    add = list(map(int,input().split()))
    graph.append(add)
    xgraph[_] += add.count(0)

for i in range(9):
    for j in range(9):
        if graph[i][j]==0:
            ygraph[j]+=1

blank = []
for i in range(9):
    for j in range(9):
        if graph[i][j]==0:
            add = ''
            if xgraph[i]==1:
                add ='X'
            elif ygraph[j]==1:
                add ='Y'
            else:
                add ='Z'
            blank.append([add,i,j])
blank=sorted(blank)

while blank:
    zero, y, x  = blank.pop(0)
    if xgraph[y] ==9 or graph[x].count(0)==9:
        blank.append(['Z',y,x])
        continue
    # 한줄 체크 먼저
    # 1) 가로확인
    if zero=='X':
        garo = list(range(1,10))
        for i in graph[y]:
            if i != 0:
                garo.remove(i)

        if len(garo)== 1:
            graph[y][x] = garo[0]
            ygraph[x]-=1
            continue


    # 2) 세로확인
    if zero =='Y':
        sero = list(range(1,10))
        for i in range(9):
            if graph[i][x] !=0:
                sero.remove(graph[i][x])
        if len(sero)==1:
            graph[y][x] = sero[0]
            ygraph[x]=0
            continue

    # 3) 9등분 확인
    else:

        if 0<=y<3 :
            ys,ye = 0,3
            if 0 <= x< 3:
                xs,xe = 0,3
            if 3 <= x < 6:
                xs,xe = 3, 6
            if 6 <= x < 9:
                xs,xe = 6,9

        elif 3<=y<6 :
            ys,ye = 3, 6
            if 0 <= x < 3:
                xs, xe = 0, 3
            if 3 <= x < 6:
                xs, xe = 3, 6
            if 6 <= x < 9:
                xs, xe = 6, 9

        elif 6<=y<9:
            ys,ye = 6,9
            if 0 <= x < 3:
                xs, xe = 0, 3
            if 3 <= x < 6:
                xs, xe = 3, 6
            if 6 <= x < 9:
                xs, xe = 6, 9

        square = list(range(1,10))
        for i in range(ys,ye):
            for j in range(xs,xe):
                if graph[i][j]!=0:
                    square.remove(graph[i][j])

        if len(square) == 1:
            graph[y][x] = square[0]
            ygraph[x]-=1
            continue

    if ygraph[x]==1:
        zero ='Y'
    elif graph[y].count(0)==1:
        zero = 'X'
    else:
        zero = 'Z'
    blank.append([zero,y,x])


for i in range(9):
    print(*graph[i])