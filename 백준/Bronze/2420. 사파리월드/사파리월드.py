a, b = map(int, input().split())

if(a > b):
    print(a - b)
elif(b > a):
    print(b - a)
else:
    print(0)