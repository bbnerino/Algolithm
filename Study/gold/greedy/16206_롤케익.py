N, count = map(int, input().split())
# 케익개수 , 자를횟수
cake = sorted(list(map(int, input().split())))
eat = 0

if 10 in cake and count == 0:
    eat = cake.count(10)

while count > 0:
    if sum(cake) == 0:
        break
    else:
        for i in range(len(cake)):
            if cake[i] % 10 == 0 and cake[i] != 0 :
                eat += cake[i] // 10
                count -= cake[i] // 10 - 1
                cake[i] = 0
                if count < 0:
                    eat += count-1
                    count=0
                    break

            if cake[i] % 10 != 0: # 10으로 안나눠지면
                if cake[i]>10: # 10이상이면
                    eat += cake[i] // 10 # 한개먹고
                    count -= cake[i] // 10 
                    cake[i] = cake[i] - 10 * (cake[i] // 10)
                    if count < 0:
                        eat += count
                        count=0
                        break
                else:
                    cake[i]=0
                    if count < 0:
                        eat += count
                        count=0
                        break
print(eat)



        

    
    