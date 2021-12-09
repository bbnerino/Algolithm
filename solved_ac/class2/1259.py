def palindrome(a):
    
    if a!=0:
        result=""
        if len(a)!=0 and len(a)!=1 :
            if a[0]==a[-1]:
                return palindrome(a[1:-1])
            else:
                result="no"
        elif len(a)==0:
            result="yes"
        else:
            result="yes"
        return result

while True:
    a=input()
    if a=="0":
        break
    
    print(palindrome(a))
