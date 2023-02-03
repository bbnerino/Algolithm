from itertools import permutations

def solution(A, B):
    A.sort()
    B.sort()
    result = 0 
    a = A.pop(0)
    while B:
      b = B.pop(0)
      if a<b :
        result += 1
        if A:
          a = A.pop(0)

    return result

A =[1,3,42,6,23,54]	
B =[2,2,34,56,6,7]

print(solution(A,B))