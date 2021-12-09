N=int(input())
if N >2:
    numlist=[0 for _ in range(N+1)]
    numlist[1]=1
    numlist[2]=2

    for i in range(3,N+1):
        numlist[i] = (numlist[i-1]+numlist[i-2]) % 15746
        # 안에 값을 넣으니 시간초과가 안난다 ? 이유?!
    print(numlist[N])
else:
    print(N)