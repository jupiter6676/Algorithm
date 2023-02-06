N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)

for i in range(N):
    end = i + schedules[i][0]

    for j in range(end, N + 1):
        dp[j] = max(dp[j], dp[i] + schedules[i][1])

print(dp[-1])