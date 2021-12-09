from collections import deque
import sys

T = int(sys.stdin.readline())
Q = deque()

for ts in range(T):
    word = input()

    if word[0:4]=="push":
        Q.append(int(word[5::]))
    elif word=="pop":
        try:
            print(Q.popleft())
        except:
            print(-1)
    elif word=="size":
        print(len(Q))
    elif word == "empty":
        if len(Q)==0:
            print(1)
        else:
            print(0)
    elif word == "front":
        try:
            print(Q[0])
        except:
            print(-1)
    elif word == "back":
        try:
            print(Q[-1])
        except:
            print(-1)

