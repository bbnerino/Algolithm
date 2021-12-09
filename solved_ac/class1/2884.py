hour,minute= map(int,input().split())

if minute-45 >= 0:
    print(hour,minute-45)
else:
    if hour == 0:
        hour_45 = 23
    else:
        hour_45 = hour -1

    minute_45 = minute+15
    print(hour_45,minute_45)