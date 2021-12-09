def lonely(int_list):
    result =[] 
    prev = 100 # previous 에 아무 값이나 대입(0~9 아닌 값)
    for i in int_list:
        if i != prev: # i가 저 값과 다르다면 
            result.append(i) # 추가를 해준다.
        prev = i #prev가 i가 된다. 
    print(result)

lonely([1,1,3,3,0,1,1]) 
lonely([4,4,4,3,3])