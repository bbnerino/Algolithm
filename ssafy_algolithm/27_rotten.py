def change_rotten_fruit(fruit_bag):
    new =[]
    for i in fruit_bag:
        if "rotten" not in i :
            new.append(i)
        else:
            new.append(i[6:].lower())
    return new
# def change_rotten_fruit(fruit_bag):
#     result = []
#     for fruit in fruit_bag:
#         fruit = fruit.replace("rotten","")
#         fruit = fruit.lower()
#         result.append(fruit)
#     return result

print(change_rotten_fruit(['apple', 'rottenBanana', 'apple'] ))
print(change_rotten_fruit(['rottenapple', 'rottenBanana', 'apple', 'rottenGrape']))