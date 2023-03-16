import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = set()
dp = [-1] * (K + 1)

for _ in range(N):
    coins.add(int(input()))

for c in coins:
    for i in range(c, K + 1):
        # if dp[i] == -1:
        if i % c == 0:
            dp[i] = i // c

        if dp[i - c] > 0:
            if dp[i] == -1:
                dp[i] = dp[i - c] + 1
            else:
                dp[i] = min(dp[i], dp[i - c] + 1)

print(dp[K])