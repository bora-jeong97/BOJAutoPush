import sys
I = sys.stdin.readline


for _ in range(100):
    try:
        print(I().rstrip())
    except:
        break
