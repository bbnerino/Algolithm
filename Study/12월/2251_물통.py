import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

A,B,C = map(int,input().split())

water = C
Acase = A
Bcase = B
Ccase = C

result = [[0,0,C]]

# [0,0,10]
def dfs(a,b,c):
    if a > 0:
        if a+b< Bcase:
            if [0,a+b,c] not in result:
                result.append([0,a+b,c])
                dfs(0,a+b,c)
        else:
            if [(a+b)-Bcase,Bcase,c] not in result:
                result.append([(a+b)-Bcase,Bcase,c])
                dfs((a+b)-Bcase,Bcase,c)

        if a+c< Ccase:
            if [0, b, a+c] not in result:
                result.append([0, b, a+c])
                dfs(0, b, a+c)
        else:
            if [(a + c) - Ccase, b, Ccase] not in result:
                result.append([(a + c) - Ccase, b, Ccase])
                dfs((a + c) - Ccase, b, Ccase)

    if b > 0:
        if a + b < Acase:
            if [a + b,0, c] not in result:
                result.append([a + b,0, c])
                dfs(a + b,0, c)
        else:
            if [Acase, (a + b) - Acase, c] not in result:
                result.append([Acase, (a + b) - Acase, c])
                dfs(Acase, (a + b) - Acase, c)

        if b + c < Ccase:
            if [a, 0, b + c] not in result:
                result.append([a, 0, b + c])
                dfs(a, 0, b + c)
        else:
            if [a,b+c-Ccase ,Ccase] not in result:
                result.append([a,b+c-Ccase ,Ccase])
                dfs(a,b+c-Ccase ,Ccase)

    if c > 0:
        if a + c < Acase:
            if [a+c,b, 0] not in result:
                result.append([a+c,b, 0])
                dfs(a+c , b, 0)
        else:
            if [Acase,b,a+c-Acase] not in result:
                result.append([Acase,b,a+c-Acase])
                dfs(Acase,b,a+c-Acase)

        if b + c < Bcase:
            if [a, b+c,0 ] not in result:
                result.append([a, b+c,0 ])
                dfs(a, b+c,0 )
        else:

            if [a, Bcase, b+c-Bcase] not in result:
                result.append([a, Bcase, b+c-Bcase])
                dfs(a, Bcase, b+c-Bcase)



dfs(0, 0, C)
rr = []
for i in result:
    if i[0]==0:
        rr.append(i[2])
print(*sorted(rr))




