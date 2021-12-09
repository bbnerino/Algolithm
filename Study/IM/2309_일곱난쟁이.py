nanjaeng=[]
for i in range(9):
    nanjaeng.append(int(input()))
out = sum(nanjaeng)-100 # 140-100 = 40
for i in range(len(nanjaeng)-1):
    for j in range(i+1,len(nanjaeng)):
        if nanjaeng[i]+nanjaeng[j]==out:
            nanjaeng.pop(i)
            nanjaeng.pop(j-1)
            break
sss = sorted(nanjaeng)

for i in sss:
    print(i)