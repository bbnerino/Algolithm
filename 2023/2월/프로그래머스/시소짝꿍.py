from itertools import combinations
################
# 시간초과
def solution(weights):
    answer = []
    new_weights = dict()    

    for w in range(len(weights)):
        for i in range(2,5):
            tmp = str(weights[w])+"-"+str(w+1)
            try:
                new_weights[weights[w]*i].append(tmp)
            except:
                new_weights[weights[w]*i] = [tmp]

    for weight_list in new_weights.values():
        if len(weight_list)>=2:
            answer.extend(list(combinations(weight_list,2)))
    
    return(len(set(answer))) 
weights = [100,180,360,100,270]
print(solution(weights))