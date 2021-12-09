num = int(input())
grade=""
if 90<num<=100:
    grade = "A"
elif 80<num<=90:
    grade = "B"
elif 70<num<=80:
    grade = "C"
elif 60<num<=70:
    grade = "D"
else :
    grade = "F"
print(grade)