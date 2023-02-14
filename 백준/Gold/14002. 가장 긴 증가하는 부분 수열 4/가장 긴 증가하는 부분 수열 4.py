N = int(input())
seq = list(map(int, input().split()))

dp = [[] for _ in range(N)]

for i in range(N):
    if not dp[i]:
        dp[i].append(seq[i])

    for j in range(i):
        if seq[j] < seq[i]:
            if len(dp[i]) < len(dp[j] + [seq[i]]):
                dp[i] = dp[j] + [seq[i]]

dp.sort(key=lambda x: -len(x))
print(len(dp[0]))
print(*dp[0])