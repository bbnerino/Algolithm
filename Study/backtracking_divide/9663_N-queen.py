import sys
sys.stdin =open('input.txt')

def queen(num):
    global count
    count =0
    if num ==N:
        count+=1
        return
    dy = [1,1,-1,-1]
    dx = [-1,1,-1,1]


    for i in sero:
        for j in garo:
            if [i,j] not in daegak:
                if graph[i][j]==0:
                    graph[i][j]=1
                    sero.remove(i)
                    garo.remove(j)

                    dae_count =0
                    for k in range(4):
                        l=1
                        while True:
                            ny = i + dy[k]
                            nx = j + dx[k]
                            if 0<=l*ny<N and 0<=l*nx<N:
                                daegak.append([l*ny,l*nx])
                                dae_count+=1
                                l+=1
                            else:
                                break

                    queen(num+1)

                    sero.append(i)
                    garo.append(j)
                    for _ in range(dae_count):
                        daegak.pop()
                else:
                    return




N = int(input())
graph = [[0]*N for _ in range(N)]

sero =list(range(N))
garo =list(range(N))
daegak =[]

queen(1)
print(count)