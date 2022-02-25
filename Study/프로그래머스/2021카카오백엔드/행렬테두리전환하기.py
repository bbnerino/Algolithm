
rows, columns = 100,97
queries =[[1,1,100,97]]



def solution(rows, columns, queries):
    graph = [[0 for _ in range(columns)] for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = num
            num += 1
    answer = []
    while queries:
        querie = queries.pop(0)
        cover = []
        covernum = []
        i = querie[0]-1
        j = querie[1]-1
        while [i,j] not in cover:
            if i == querie[0]-1:
                if j<querie[3]:
                    cover.append([i,j])
                    covernum.append(graph[i][j])
                    j+=1
                else: # i는 첫줄 j 가 넘어서면?
                    j-=1
                    i+=1
                    while i < querie[2]:
                        cover.append([i, j])
                        covernum.append(graph[i][j])
                        i+=1
            elif i == querie[2]:
                i-=1
                j-=1
            elif i < querie[2]:
                if j >=querie[1]-1:
                    cover.append([i, j])
                    covernum.append(graph[i][j])
                    j-=1
                else:
                    j+=1
                    i-=1
                    while i > querie[0]:
                        cover.append([i, j])
                        covernum.append(graph[i][j])
                        i-=1

        covernum.insert(0,covernum.pop())
        answer.append(min(covernum))
        for m in range(len(covernum)):
            graph[cover[m][0]][cover[m][1]] = covernum[m]

    return answer


print(solution(rows,columns,queries))


