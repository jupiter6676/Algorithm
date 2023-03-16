import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = set()

for _ in range(N):
    coins.add(int(input()))

dp = [10001] * (K + 1)
dp[0] = 0   # 0원을 만드는 동전의 수는 0개

for c in coins:
    for i in range(c, K + 1):
        dp[i] = min(dp[i], dp[i - c] + 1)

print(dp[K] if dp[K] != 10001 else -1)