n, x = map(int, input().split())
arr = map(int, input().split())
arr = list(arr)
for i in range(0, n):
    if(arr[i] < x):
        print(f"{arr[i]} ", end='')