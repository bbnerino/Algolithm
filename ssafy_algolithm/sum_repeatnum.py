def sum_of_repeat_number(numbers):
    total =0
    for i in numbers:
        if numbers.count(i) == 1:
            total += i
    return total

print(sum_of_repeat_number([4, 4, 7, 8, 10]))