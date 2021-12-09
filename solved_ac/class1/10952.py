a,b=(0,0)
while 1:
    try:
     a,b=map(int,input().split())
     if (a, b) == (0, 0):
         break;
     print(a+b)

    except:
     break;