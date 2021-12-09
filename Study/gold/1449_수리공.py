N,L= map(int,input().split())
# 테이프길이 L
hole= sorted(list(map(int,input().split(" "))))
tape= 0
count=0
i=0
while i<len(hole) :
    if i!=len(hole)-1:
        for j in range(i+1,len(hole)):
            if L >hole[j]-hole[i] > tape :
                tape =  hole[j]-hole[i]
                if j==len(hole)-1:
                    count+=1
                    i=j+1
                    break
            else:
                tape=0
                count+=1
                i = j
                break
    else:
        count += 1
        i += 1
        break

print(count)