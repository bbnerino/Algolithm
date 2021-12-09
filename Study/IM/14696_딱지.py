def winner(A, B):
    global win
    if len(A) > 0 and len(B) > 0:
        ap = A.pop()
        bp = B.pop()
        if ap > bp:
            win = "A"
            return

        elif ap < bp:
            win = "B"
            return
        else:
            winner(A, B)
    else:
        if len(A) == 0 and len(B) == 0:
            win = "D"
            return
        elif len(A) == 0:
            win = "B"
            return
        elif len(B) == 0:
            win = "A"
            return
    

win = ""
T = int(input())
result = []
for ts in range(T):
    A = sorted(list(map(int, input().split()))[1::])
    B = sorted(list(map(int, input().split()))[1::])
    winner(A, B)
    result.append(win)
for ts in range(T):
    print(result[ts])