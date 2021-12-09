T= int(input())
white = [[0]*100 for _ in range(100)] # 100 100 만들고
for ts in range(T):
    x,y = map(int,input().split())
    for i in range(x,x+10): # x~ x+10 까지 색칠
        for j in range(y,y+10):
            white[i][j] = 1 # 1로 바꿔준다
total =0
for i in range(100):
    for j in range(100):
        if white[i][j]==1: # 1의 개수를 구하면 됩니다.
            total+=1
print(total)

    
