def my_abs(x):
    if type(x) == int or type(x) == float:
        if x >=0:
            return x
        else :
            return -x 

    elif type(x) == complex:
        return (x.imag**2 + x.real**2)**(1/2)

print(my_abs(3+4j))
print(my_abs(-0.0))
print(my_abs(-5))
print(abs(3+4j), abs(-0.0), abs(-5))

def my_all(elements): #### 교수님답 , 비어있으면 True! 
    for ele in elements:
        if not ele:
            return False
    return True 


print(my_all([])) #순회할 정보가 없으면 실행이 안됨 
print(my_all([1, 2, 5, '6']))
print(my_all([[], 2, 5, '6']))
print(all([]), all([1, 2, 5, '6']), all([[], 2, 5, '6']))

def my_any(elements): ### 교수님 답 
    #모든 요소가 False일 때만 False
    for ele in elements:
        if elements:
            return True
    return False


print(my_any([1]))
print(my_any([1, 2, 5, '6']))
print(my_any([[], 2, 5, '6']))
print(my_any([0]))
print(any([1, 2, 5, '6']), any([[], 2, 5, '6']), any([0]))


