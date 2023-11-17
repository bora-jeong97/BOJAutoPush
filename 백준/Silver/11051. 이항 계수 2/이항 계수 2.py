import sys
sys.setrecursionlimit(10 ** 6)
MOD = 10007



cache = [[0] * 1001 for _ in range(1001)]   # 최대값까지 안나오는 값으로 초기화
N, K = map(int, input().split())


# 재귀
def bino(n, k):
    if cache[n][k]:
        return cache[n][k]

    if k == 0 or k == n :   # 무한히 반복되는 것을 막기 위한 이항계수 정의
        cache[n][k] = 1
    else:
        cache[n][k] = bino(n - 1, k - 1) + bino(n - 1, k)

    return cache[n][k]

print(bino(N, K) % 10007)