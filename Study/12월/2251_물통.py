import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

Acase,Bcase,Ccase = map(int,input().split())  # 케이스의 크기를 입력 받는다



result = [[0,0,Ccase]]            # 나올수 있는 모든 결과값

# 시작 0,0,10
# a,b,c 중에 물이 남아있는 곳이 있다면, 다른 곳으로 붓는다.
# 그 결과가 이전의 결과값에 포함 되어 있다면 무시하고,
# 이전의 결과값에 없다면, 붓고, 그 값으로 새로운 dfs가 시작된다

def dfs(a,b,c):
    if a > 0:               # acase 에 물이 남아있는 경우
        # bcase 로 붓는데 ,
        if a+b< Bcase:      # 두 통의 물의 합이 bcase보다 작다면?
                            # [0, a+b , c] (a에서 b로 그냥 따르기, c는 그대로)
            if [0,a+b,c] not in result:    # 결과값에 없다면?
                result.append([0,a+b,c])   # 결과값  추가 + 새로운 dfs 시작
                dfs(0,a+b,c)
        else:               # 두 통의 물의 합이 bcase보다 크다?
                            # [(물의합 - B통 크기), B통 크기, c ]
                            # -> [(a+b)-Bcase,Bcase,c]
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



dfs(0, 0, Ccase)
final = []
# 나올 수 있는 모든 값
# [0, 0, 10], [8, 0, 2], [0, 8, 2], [2, 8, 0]
# [1, 9, 0],  [0, 9, 1], [8, 1, 1], [0, 1, 9]
# [1, 0, 9],  [8, 2, 0], [0, 2, 8], [2, 0, 8]
for i in result:
    if i[0]==0:             # A가 비어있을 때
        final.append(i[2])  # C값 넣어주기
print(*sorted(final))       # 정렬하기




