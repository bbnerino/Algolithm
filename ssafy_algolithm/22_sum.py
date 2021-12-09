# 자연수 number를 입력 받아, 각 자릿수의 합을 계산하여 출력하시오.

# def sum_of_digit(number):
#     string = str(number)
#     sum = 0
#     for i in range(len(string)):
#         sum += int(string[i])
#     return sum 

def sum_of_digit(num):
    sum = 0
    while num != 0:
        sum += num%10
        num //= 10
    return sum 
print(sum_of_digit(12345))
print(sum_of_digit(43211))

