array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    while commands:
        s,e,k = commands.pop(0)
        new = array[s-1:e]
        new.sort()
        answer.append(new[k-1])
    return answer

print(solution(array,commands))