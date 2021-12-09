N= int(input())
stage=[]
for i in range(N):
    stage.append(int(input()))

count= 0
for i in range(len(stage)-1,0,-1):
    if stage[i] > stage[i-1]:
        pass
    else:
        count += stage[i-1] - (stage[i]-1)
        stage[i-1] = stage[i]-1
print(count)