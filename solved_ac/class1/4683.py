every = list(range(1,10000))

for i in range(1,10000):
    i = int(i)
    if i<10:
        every.remove(2*i)
    if 10<=i<100:
        try:
            every.remove((i%10)+(i//10)+i)
        except:
            pass
    if 100<=i<1000:
        hun = i//100
        ten = (i - hun*100)//10
        one = (i - hun*100 - ten*10)%10
        try:
            every.remove(i+hun+ten+one)
        except:
            pass
    if 1000<=i <10000:
        thous =i//1000
        hun = (i-thous*1000)//100
        ten = (i-thous*1000 - hun*100)//10
        one = (i-thous*1000 - hun*100 - ten*10)%10
        try :every.remove(i+thous+hun+ten+one)
        except:
            pass
for j in every:
    print(j)

