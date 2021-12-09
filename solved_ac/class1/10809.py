word = input()
# print(ord("z")) # a=97,=> 0 (-97) , z=122 => 25
for eng in range(26):
    if chr(eng+97) in word: # chr(eng+97) == ab...z
        print(word.find(chr(eng+97)),end=" ")
        
    else:
        print(-1,end=" ")