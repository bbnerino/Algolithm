#두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 
# 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

#수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
nums=[]
for i in range(10):
    nums.append(int(input()))
    #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result=[]
for i in range(10):
    result.append((nums[i]) % 42)
# result [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = []
for i in range(len(result)):
    if result[i] not in sum:
        sum.append(result[i])
# print(sum) [39, 40, 41, 0, 1, 2]
print(len(sum))