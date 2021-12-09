N = int(input())
# 버퍼의 크기
nums = []
while True:
    T = int(input())
    if T ==0:
        try: # 내용이 있다면 pop(0)을 해준다
            nums.pop(0) 
        except:
            pass
    elif T == -1: 
        break
    else:
        if len(nums)<N: # 라우터 길이를 벗어나면 넣지 않는다
            nums.append(T)
        else:
            pass
if len(nums)!=0:
    print(*nums)  
else:
    print("empty")  