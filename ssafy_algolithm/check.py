def check(n,students):
    students =students.replace(" ","")
    everyone =[]
    for i in range(n):
        everyone.append(i+1) # 1234567
    
    for j in students: # 135
        if int(j) in everyone:
            everyone.remove(int(j)) 
    
    return everyone
print(check(7, '1 3 5')) # 2 4 6 7