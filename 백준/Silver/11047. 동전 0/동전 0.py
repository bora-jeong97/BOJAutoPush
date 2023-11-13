# Ai는 Ai-1의 배수
# 위 말때문에 그리디로 풀 수 있음
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()

ans = 0 # 몇개 남았는지
for coin in coins:
    ans += K // coin # 코인으로 나눈 몫
    K %= coin # 나머지




print(ans)