import sys
inp = sys.stdin.readline
T = int(input())

for i in range(0, T, 1):
    a, b = map(int, inp().split())
    print(a+b)