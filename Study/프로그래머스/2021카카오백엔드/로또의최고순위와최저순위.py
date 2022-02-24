def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    #     0등,1등... 6등=1개, 7등 0개
    result = 0
    zero = 0
    for i in lottos:
        if i != 0:
            if i in win_nums:
                result += 1
        else:
            zero += 1

    answer = [0, 0]
    answer[0] = rank[result + zero]
    answer[1] = rank[result]
    return answer