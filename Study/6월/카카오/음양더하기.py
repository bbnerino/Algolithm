absolutes = [4,7,12]
signs = ['true','false','true']

def solution(absolutes, signs):
    answer = 0
    minus = 1
    for i in range(len(absolutes)):
        if not signs[i] :
            minus = -1
        else:
            minus = +1
        answer += int(absolutes[i]) * minus
    return answer

print(solution(absolutes,signs))