N=int(input())
wordlist=[]

for i in range(N):
    wordlist.append(input())
wordlist=list(set(wordlist))

book={}
for i in wordlist:
    if book[len(i)]!=None:
        book[len(i)]=[i]
        
    else:    
        book[len(i)].append(i)
print(book)
print(book.keys()) #dict_keys([2, 1, 4, 6, 3, 8, 5])

for i in sorted(book.keys()):
    print(book.get(i),)