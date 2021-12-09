def dict_invert(my_dict):
    result = {}
    for key, val in my_dict.items():
        if val in result:
            result[val].append(key)
        else:
            result[val] =[key]
    return result
    # 넘겨받는 값 모두 순회
    # 내가 지금 피요한건 key, value
    # 하지만 딕셔너리를 순회하면 얻을 수 있는 건? key
    # 그럼 key로 조회해서 value 찾으면 된다.
    # 근데 순회할 때 한번에 key 랑 value를 같이 찾아오는 애 있다.
    # 새 딕셔너리에 이전 dict의 밸류를 키로 하는 요소가 있는지 찾는다
    
# def dict_inver(my_dict):
#     result ={}
#     for key,val in my_dict.items():
#         result[val] =result.get(val,[]) + [key]

#     return result



print(dict_invert({1: 10, 2: 20, 3: 30}))
print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30}))
print(dict_invert({1: True, 2: True, 3: True}))