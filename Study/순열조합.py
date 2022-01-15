# N자리 M진수를 만들거다.!
# 3자리 4진수를 만들면
# ex) 000 001 002 ... 333

'''
# 1번 템플릿 (완전탐색)
n = int(input())
m = int(input())
data = [0]*n

def recur(cur):
    # 종료조건 => 어떻게 되면 이 recur 함수를 종료를 시키겠다!!
    if cur == n:
        print(data)
        return

    # 재귀호출부 (재귀를 어떻게 해서 실행시킬건지!!)
    for i in range(m):
        data[cur] = i
        recur(cur+1)

recur(0)
'''




'''
# 2번 템플릿
# 순열 N자리 M진수 => 순서에 의미가 있는것!
# 숫자의 중복이 없어야해!!!  =>>> 방문처리를 해줘야한다!!
n = int(input())
m = int(input())
data = [0] * n
visited = [False] * m

def recur(cur):
    # 종료조건
    if cur == n:
        print(data)
        return

    for i in range(m):
        if visited[i]:
            continue

        visited[i] = True
        data[cur] = i
        recur(cur+1)
        visited[i] = False

recur(0)
'''
'''
# 3번 템플릿
# 조합 -=> 순서에 의미가 없어!! -> 오름차순으로 만들어야지 순서까지 다 제거가 가능!!
n = int(input())
m = int(input())
data = [0] * n

def recur(cur, start):
    # 종료조건
    if cur == n:
        print(data)
        return

    # 조합을 나타낼 재귀호출부!!
    for i in range(start, m):
        data[cur] = i
        recur(cur+1, i+1)

recur(0, 0)
'''
n = 3
m = 6
data = [0]*n

def recur(cur,start):
    if cur==n:
        print(data)
        return 
    for i in range(start,m):
        data[cur] = i
        recur(cur+1,i+1)

recur(0,0)


# 4번 템플릿
# 조합 => 쓴다 or 안쓴다 => 결과 도출

n = int(input())
m = int(input())
data = []

def recur(cur, cnt):
    # 종료 조건
    # 1. 숫자를 n번 쓰고 / 내가 숫자를 쓸때마다 cnt를 1씩 추가하겠다.
    if cnt == n:
        # for i in range(n):
        #     print(data[i], end = '')
        # print('')
        print(data)
        return
        
    # cur 깊이가 우리가 쓸 숫자 끝까지 도착하면 return
    if cur == m:
        return

    # 재귀호출부
    data.append(cur)
    recur(cur+1, cnt+1)
    data.pop()
    recur(cur+1, cnt)

recur(0, 0)