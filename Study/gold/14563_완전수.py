for num in range(1,10000):
    yak = []
    for i in range(1,num):
        if num%i==0:
            yak.append(i)

    # print(yak)
    # [1, 2, 4, 7, 14]
    # [1, 3, 7]
    # [, 18,123,132,321,123,1423,4132,1203123,.123123,123]  
    
    if sum(yak)==num:
        if len(yak)<=10:
            print(num,end="=")
            print("+".join(map(str,yak)))
        elif len(yak)>10:
            print(num,end="=")
            while len(yak) > 10:
                print("+".join(map(str,yak[0:10])))

                for i in range(10):
                    yak.pop(0)
            print("+".join(map(str,yak)))
                

# 33550336 를 찾기위해서는 3000만번 * 3000만번의 계산을 거쳐야합니다.
# 좋은 방안이 떠오르지 않아 제외하겠습니다.
        

# extra = 33550336
# yak = []
# for i in range(1,extra):
#     if num%i==0:
#         yak.append(i)
    
#     if sum(yak)==num:
#         print("+".join(map(str,yak)),end="=")
#         print(num)


def is_perfectNumber(i):
    divisor = [] # 1,2,3
    for n in range(1,i):
        if i%n == 0 :
            divisor.append(n)
    if sum(divisor) == i:
        return divisor


for j in range(1, 10000):
    if is_perfectNumber(j):
        print(j,"=")

       
