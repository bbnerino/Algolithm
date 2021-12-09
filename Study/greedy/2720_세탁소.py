# quarter =0.25
# dime = 0.10
# nickel = 0.05
# penny = 0.01
T= int(input())
result=[[] for _ in range(T)]
for ts in range(T):
    money=int(input())
    # 124 원 25 원 194원
    # 25 원 10 원 5원 1원
    result[ts].append(money//25)
    money-= 25*(money//25)
    result[ts].append(money//10)
    money-= 10*(money//10)
    result[ts].append(money//5)
    money-= 5*(money//5)
    result[ts].append(money//1)
    money-= 1*(money//1)

# print(result) [[4, 2, 0, 4], [1, 0, 0, 0], [7, 1, 1, 4]]

for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j],end=" ")
    print()
