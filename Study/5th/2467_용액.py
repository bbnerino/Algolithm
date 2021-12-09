import sys
sys.stdin= open('input.txt')

N = int(input())
liquid = list(map(int,input().split()))



s = 0
e= N-1
result = [0,0,liquid[0]+liquid[-1]] # 결과값은 미리 만들어둔다 

            #
while s<e:  # s와 e가 서로 다가오는데 s와 e가 같아지면 안된다.
    if abs(result[2]) >= abs(liquid[s]+liquid[e]) : # 우리가 찾을 절대값이 위의 결과값의 절대값보다 작다면?  
        result = [s, e, liquid[s] + liquid[e]]      # 결과값을 바꿔준다

    if liquid[s] + liquid[e] <= 0:  # s의 값과 e의 값의 합이 음수일 경우
        s += 1                      # s를 늘려준다 -> 값이 커진다
    elif liquid[s] + liquid[e] > 0: #
        e -= 1
    else:
        break

print(min(liquid[result[0]],liquid[result[1]]),max(liquid[result[0]],liquid[result[1]]))

