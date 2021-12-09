square=[]
for ts in range(4):
    rectangle= list(map(int,input().split()))
    square.append(rectangle)
# [[1, 2, 4, 4], [2, 3, 5, 7], [3, 1, 6, 5], [7, 3, 8, 6]]

paper=[[0]*100 for _ in range(100)]
for sq in square:
    for i in range(sq[0],sq[2]):
        for j in range(sq[1],sq[3]):
            paper[i][j]=1
total=0
for i in paper:
    total+=i.count(1)
print(total)
        
