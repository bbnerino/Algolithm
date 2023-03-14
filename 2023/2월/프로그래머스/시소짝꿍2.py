from itertools import combinations

def solution(weights):
    answer = 0
    combis = [
      [2,2],[2,3],[2,4], 
      [3,2],[3,3],[3,4],
      [4,2],[4,3],[4,4]
    ]
    weights = list(combinations(weights,2))
    for weight in weights:
        for combi in combis :
            if combi[0]*weight[0] == combi[1]*weight[1]:
                answer+=1
                break
            

    return answer

    
weights = [100,180,360,100,270]
print(solution(weights))


