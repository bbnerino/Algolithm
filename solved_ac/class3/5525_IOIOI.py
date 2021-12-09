N= int(input())
l=int(input())
quest = input()

find = ["I" for _ in range(N+1)]
find="O".join(find)
length= len(find)
def IOIO(num):
    global count
    if quest[num]=="I" and quest[num+length-1]=="I":
        if quest[num:num+length]==find:
            count+=1
    else:
        pass
count=0
for i in range(len(quest)-length):
    IOIO(i)
print(count)
