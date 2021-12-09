def combi(arr,n):
    result = []

    if n ==0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        rest_arr = arr[i+1:]
        for C in combi(rest_arr,n-1):
            result.append([elem]+C)
    return result
print(combi([1,2,3,4],2))