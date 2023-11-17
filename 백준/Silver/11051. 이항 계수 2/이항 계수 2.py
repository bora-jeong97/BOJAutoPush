'''이항계수'''
MOD = 10007

cache = [[0] * 1001 for _ in range(1001)]   # 최대값까지 안나오는 값으로 초기화
N, K = map(int, input().split())

# 반복문
for i in range(1001):
    cache[i][0] = cache[i][i] = 1
    for j in range(1, i):
        cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
        cache[i][j] %= MOD


print(cache[N][K])