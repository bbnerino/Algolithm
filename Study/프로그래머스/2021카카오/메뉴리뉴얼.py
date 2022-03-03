orders =["XYZ", "XWY", "WXA"]
course = [2,3,4]
import sys
input = sys.stdin.readline

def solution(orders, course):
    from itertools import combinations
    longest = 0
    for order in orders:
        longest =max(longest,len(order))
    results = []

    for each in course: # 2,3,4 하나하나를 돌면서
        if each > longest:
            break
        combis = []
        for order in orders:
            order=sorted(order)
            if len(order)>=each:
                tmp = set(sorted(list(combinations(order,each))))
                combis.extend(tmp)
        combis = list(set(combis))

        # 2개인 조합들 [A,D],[A,E]...
        big = []
        bignum = 0
        for combi in combis: # 조합 한 덩이씩 확인 [A,D]
            tmpnum = 0
            for orderlist in orders: # 처음 전체 덩어리 하나하나 확인
                flag = True
                for c in combi: # 조합덩어리의 한개씩 확인 A, D
                    if flag:
                        if c not in orderlist: # 덩어리에 없다면
                            flag = False
                    else:
                        break
                if flag:
                    tmpnum+=1
            if tmpnum  >bignum:
                bignum = tmpnum
                big = []
            if tmpnum == bignum and tmpnum>1:
                big.append(combi)
        results.append(big)

    answer = []
    for result in results:
        for res in result:
            tmp = ""
            for i in res:
                tmp+=i
            answer.append(tmp)
    answer.sort()
    return answer


print(solution(orders,course))
