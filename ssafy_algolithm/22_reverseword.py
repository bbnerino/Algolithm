def is_pal_while(word):
    result = ""
    i = len(word) - 1
    while i>=0:
        result+= word[i]
        i-=1
    return result

# print(is_pal_while('tomato'))
# print(is_pal_while('racecar'))
# print(is_pal_while('azza'))

def is_pal_recursive(word): # 하석code 참조
    if len(word)==0:
        return True
    elif word[0]==word[-1]:
        return is_pal_recursive(word[1:-1])
    else:
        return False

print(is_pal_recursive('tomato'))
print(is_pal_recursive('racecar'))
print(is_pal_recursive('azza'))