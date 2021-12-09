T = int(input())
result =[]
for ts in range(T):
    N,M = map(int,input().split())
    # N = 문서의 개수
    # M = 몇번째로 인쇄되었는지 궁금한 문서가 현재 놓여있는 곳
    files = list(map(int,input().split()))
    for i in range(len(files)):
        files[i]=[i,files[i]]
    # [[0, 1], [1, 1], [2, 9], [3, 1], [4, 1], [5, 1]]
    # 중요도가 주어진다.
    wannafind = files[M]
    count = 0
    while True:
        big = 0
        for i in range(len(files)):
            if files[i][1]>big:
                big = files[i][1]
        index = files.pop(0)
        if index[1] == big:
            count+=1
            if index == wannafind:
                break
        else:
            files.append(index)
    result.append(count)
for i in result:
    print(i)