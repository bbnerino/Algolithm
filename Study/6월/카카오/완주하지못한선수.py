participant = ["leo", "kiki", "eden"]
completion  = ["eden", "kiki"]


def solution(participant, completion):
    answer = ''
    part = sorted(participant)
    comp = sorted(completion)
    for i in range(len(comp)):
        if comp[i] != part[i]:
            answer = part[i]
            break
    if answer =='':
        answer = part[-1]
    return answer


print(solution(participant,completion))