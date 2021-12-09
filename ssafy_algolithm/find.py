def my_find(text, alphabet):
    result = []
    if alphabet in text:
        for i in range(len(text)):
            if text[i]== alphabet:
                result.append(i)

    else: 
        result =(text.find(alphabet))

    return result

    print(my_find('apple', 'p'))
print(my_find('a', 'p'))