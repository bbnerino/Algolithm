music = [int(x) for x in input().split()]
def updown(music):
    
    result = []
    for i in range(len(music)-1):
        if music[i]+1 == music[i+1]:
            result.append("up")
        elif music[i]-1 == music[i+1]:
            result.append("down")
        else :
            result.append("mix")
    return result
# print(updown(music))
# ['up', 'up', 'up', 'up', 'up', 'up', 'up']
if updown(music).count("up")==7:
    print("ascending")
elif updown(music).count("down")==7:
    print("descending")
else:
    print("mixed")