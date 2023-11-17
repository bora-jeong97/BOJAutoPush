N = int(input())

# 메모이제이션
cache = [-1] * 91
cache[0] = 0
cache[1] = 1

# bottom-up 반복문
for i in range(2, N+1): # 2부터 N까지
    cache[i] = cache[i-1] + cache[i-2]

print(cache[N])    