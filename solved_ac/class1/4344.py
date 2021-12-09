c=int(input())
for i in range(c):
    score = list(map(int,input().split()))
    nums= score[0] #학생수
    student =score[1:]
    average = (sum(student))/(nums) 
    total=0
    for s in student:
        if s > average:
            total+=1
    percent = f"{(total/nums)*100:.3f}%"
    print(percent)
    