import sys
sys.stdin= open('input.txt')

T = int(input())
symbols = ['+','-',' ']

def ADD(time,message):
    if len(message) == 2*N -1:
        everynums.append(message)
        return
    else:
        for symbol in symbols:
            message2 = message + symbol + str(numlist[time])
            ADD(time+1,message2)

for tc in range(T) :
    N = int(input())
    numlist = list(range(1,N+1))
    everynums = []
    ADD(1,str(numlist[0]))
    result =[]
    for num in everynums:
        nnum = num.replace(" ","")
        nnum = nnum.replace("-","+-")
        newnum = nnum.split("+")

        check = 0
        for i in newnum:
            check += int(i)
        if check ==0:
            result.append(num)
    result = sorted(result)

    for r in result:
        print(r)

    print()


