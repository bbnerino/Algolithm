N=int(input())
rope=[int(input()) for _ in range(N)]
rope.sort() # [5 10 15 20 ] 
result=0 # 메모리 초과 방지를 위해 [] 에서 값으로 만들었음
gob=N # 곱 = 4개

# 가장 짧은 로프 X 로프의 개수 = result

# 로프 5, 10 , 15 , 20 에서
# 선이 4개 있고 , 5가 가장 작은 수 -> 5x4 =20 (result)
for r in range(len(rope)):      # gob = 4 * (최소길이 5)가 result 보다 크면 
    if  result<= gob * rope[r]: # 만약 이 값이 현재 result 보다 크면
        result= gob * rope[r]   # result가 바뀌고 
        gob -=1                 # r이 바뀌니깐 로프개수(gob) 도 줄어든다
    else:
        gob -=1                 # result가 안바껴도 로프개수는 줄어든다.
print(result)



# import sys
# N= int(sys.stdin.readline())

# rope=[]
# for ts in range(N):
#     rope.append(int(sys.stdin.readline())) 
# result=[]

# if len(rope)>2: # 3개 부터? 
#     gob = N # 곱=4
#     while len(rope)>1:
#         small=min(rope)
#         for g in range(gob,1,-1):
#             result.append(small*g)
#         gob -= 1
#         rope.remove(small)
#     result=max(result)
# else: # 두개일때
#     for i in rope:
#         result.append(2*i)
#     if result[0]>= result[1]:
#         result=result[1]
#     else:
#         result=result[0]
# print(result)


# import sys
# N= int(sys.stdin.readline())

# rope=[]
# for ts in range(N):
#     rope.append(int(sys.stdin.readline())) 
# rope= sorted(rope)

# result=[]

# if len(rope)>2: # 3개 부터? 

#     # [5 10 15 20 ] 
#     gob = N # 곱=4
#     for i in range(len(rope)):
#         # 한개한개를 순회
#         for g in range(gob,1,-1):
#             result.append(rope[i]*g)
#         gob -= 1   
#             # 5 -> 20 15 10
#             # 10 -> 30 20 
#             # 15 -> 30 
#     result= sorted(result)[-1]

# else: # 두개일때
#     result=2*rope[0]
# print(result)


