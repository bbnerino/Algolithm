def only_square_area(a,b):
    result =[]
    for i in a:
        for j in b:
            if i==j:
                result.append(int(i)**2)
    print(result)
    

only_square_area([32,55,63],[13,32,40,55])