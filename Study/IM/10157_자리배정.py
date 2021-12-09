C ,R = map(int,input().split())
find =int(input())
movie = [[0]*C for _ in range(R)]
sx,sy=0,R-1
people=1
direct=0
if find>C*R:
    print(0)
else:
    while people<find:
        movie[sy][sx] = people
        dy=[-1,0,1,0]
        dx=[0,1,0,-1]
        direct%=4
        sy = sy + dy[direct]
        sx = sx + dx[direct]

        if 0<=sx<C and 0<=sy<R and movie[sy][sx]==0:
            people+=1
        else:
            sy -= dy[direct]
            sx -= dx[direct]
            direct+=1

    print(sx+1,R-sy)