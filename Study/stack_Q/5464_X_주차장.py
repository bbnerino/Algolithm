N, M = map(int, input().split())
parkinglot = [0 for _ in range(N)]
fee = []  # 5 2
car_weight = []  # 100 500 1000 2000
for _ in range(N):
    fee.append(int(input()))
    # 1번째 줄의 가격 2 , 3 , 5
for _ in range(M):
    car_weight.append(int(input()))

cars = []
for _ in range(2 * M):
    cars.append(int(input()))
    # 양수면 i가 들어오는 것
result = 0
while cars:
    car = cars.pop(0)
    if car > 0:
        is_in = False
        for p in range(N):
            if parkinglot[p] == 0:
                parkinglot[p] = car
                is_in = True
                break
        if is_in == False:
            cars.append(car)
    else:
        out = abs(car)
        if out in parkinglot:
            result += car_weight[out-1] * fee[parkinglot.index(out)]
            parkinglot[parkinglot.index(out)] = 0

        else:
            cars.append(car)

print(result)




