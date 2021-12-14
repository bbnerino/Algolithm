import sys
sys.stdin =  open('input.txt')
input = sys.stdin.readline

N,S  = map(int,input().split())
nums = list(map(int,input().split()))

def findsum():
    end = 0                             # 시작점
    result = 9999999999                 # 결과 = 길이
    sumnum = 0                          # 총합

    for start in range(N):              # start 지점을 0부터 ~ 끝까지 돌면서
        while True:                     # 될때까지 하겠다
            sumnum += nums[end]         # 끝점의 위치를 총합에 더한다
            if sumnum >=S:              # 만일 그 총합이 기준을 넘겼다면
                result = min(result,end-start+1)  # 결과값이 그 전의 값보다 짧은지 확인한다.
                end = start+1           # end 초기화
                sumnum = 0              # 총합 초기화
                break                   # 이미 넘었으니 더이상 end 늘릴필요없다

            else:                       # 기준을 못넘겼다면
                end+=1                  # end 늘려준다
                if end == N:            # 끝까지 갔다면?
                    end = start+1       # end 초기화
                    sumnum=0            # 총합 초기화
                    break
    if result == 9999999999:
        return 0
    else:
        return result
print(findsum())



