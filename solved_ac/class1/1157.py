word = input()
count_small = []
count_big = []

for i in range(26):
    count_small.append( word.count(chr(i+97)))
for j in range(26):
    count_big.append(word.count(chr(j+65)))
count_max = [x+y for x,y in zip(count_small,count_big)]
result =int(count_max.index(max(count_max)))

if count_max.count(max(count_max)) > 1:
    print("?")
else:
    print(chr(result +65))
