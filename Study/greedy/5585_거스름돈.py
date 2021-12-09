# 500 100 50 10 5 1

money = int(input())
money=1000-money

obaek = money//500
money-= 500*obaek

baek = money//100
money-= 100*baek

osip = money//50
money-= 50*osip

sip = money//10
money-= 10*sip

five = money//5
money-= 5*five

one = money//1
money-= one

print(obaek+ baek + osip + sip + five + one)

