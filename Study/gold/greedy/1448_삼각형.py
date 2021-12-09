N= int(input())
triangle=sorted([int(input()) for _ in range(N)])

# ['2', '2', '2', '3', '3', '4']
end = triangle[-1]  # 제일 큰 값을 가져옴
mid = triangle[-2] # 두번째고 큰 값을 가져옴
start = triangle[-3] # 세번째로 큰 값
length= -1 # 세 길이의 합

while len(triangle)>=3: # 삼각형 리스트에 3개가 남을 때 까지
    if start+mid > end: # 제일 큰 값이 합보다 더 작다면
        length = start+mid+end # 세길이의 합 나옴
        break
    else: # 두 합이 더 크다면
        try:
            triangle.pop() # 제일 큰 값을 뽑아냄
            end = triangle[-1] 
            mid = triangle[-2]
            start = triangle[-3]
        except:
            break
print(length)