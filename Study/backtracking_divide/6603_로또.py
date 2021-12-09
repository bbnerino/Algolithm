import sys
sys.stdin= open('input.txt')

def combi(arr,n):
    result =[]
    if n==0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        rest_arr = arr[i+1:]
        for C in combi(rest_arr,n-1):
            result.append([elem]+C)
    return result



while True:
    nums = list(map(int,input().split()))
    N = nums.pop(0)
    if N ==0: break
    for r in combi(nums,6):
        print(*r)
    print()