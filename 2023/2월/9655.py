import sys
sys.stdin = open("./2023/2월/input.txt")

N = int(input())
def winner(N):
  if N%2==0:
    return "CY"
  return "SK"

print(winner(N))