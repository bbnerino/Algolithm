import sys
sys.stdin =open('input.txt')
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
count = [0,0,0]
# [0,1,-1]
stack=[[0,0]]

def paper(N):

    s = stack.pop()
    check = True
    num = graph[s[0]][s[1]]

    for i in range(s[0], s[0]+N):
        if check == False:
                break
        for j in range(s[1], s[1]+N):
            if graph[i][j] != num:
                check = False
                break

    if check ==True:
        count[num]+=1

    else:
        N = N //3
        for i in range(s[0],s[0]+N*3, N ):
            for j in range(s[1],s[1]+N*3, N ):
                stack.append([i,j])
                paper(N)

                # Q.append([i,j])

paper(N)

print(count[-1])
print(count[0])
print(count[1])

        
