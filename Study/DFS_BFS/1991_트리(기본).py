def pre_order(n):
    if n:
        print(chr(n+64),end='')
        pre_order(left[n])
        pre_order(right[n])
def in_order(n):
    if n:
        in_order(left[n])
        print(chr(n+64),end='')
        in_order(right[n])
def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        print(chr(n+64),end='')

N = int(input())
left =[0]*27
right =[0]*27

for ts in range(N):
    p,l,r = input().split()
    if l!=".":
        left[ord(p)-64] = ord(l)-64
    if r!=".":
        right[ord(p)-64]= ord(r)-64
    
pre_order(1)
print()
in_order(1)
print()
post_order(1)

# print(ord('A'))# 65
