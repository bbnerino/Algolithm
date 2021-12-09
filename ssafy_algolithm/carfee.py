def fee(minute, distance):
    daeyeo = minute*1200 
    if minute%30 == 0:
        boheom=(minute//30)*525
    else:
        boheom=((minute+1)//30)*525
    if distance< 100:
        joohaeng = 170*distance
    else:
        joohaeng = 17000+ (distance-100)*(170/2)
    result = daeyeo + boheom + joohaeng
    return result
    
    print(fee(600, 50))
print(fee(600, 110))