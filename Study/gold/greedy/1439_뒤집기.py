zeroone=input()

no_zero = list(zeroone.split("0"))  # 0을 기준으로 나눈다
# ['', '', '', '11', '', '']
while "" in no_zero: # 빈칸제거
    no_zero.remove("")
# ['11']
small=len(no_zero) # 11 을 뒤집으면 최소 개수다 


no_one = list(filter(None,zeroone.split("1"))) # 1을 기준으로 나눈다

if len(no_one)< small:
    small = len(no_one)
# ['000', '00']
print(small)
