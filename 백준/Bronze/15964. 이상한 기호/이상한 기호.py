def gol(a, b):
    return (a+b)*(a-b)

n1, n2 = map(int, input().split())
print(gol(n1, n2))