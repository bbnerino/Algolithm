def duplicated_letters(word):
    word = list(word)
    result = []
    for i in word:
        if word.count(i) > 1:
            result.append(i)
    result = list(set(result)) # 셋으로 바꿔 중복 제거 -> 다시 리스트로
    print(result)
    
    
duplicated_letters('apple') # ['p']
duplicated_letters('banana')# ['a','n']