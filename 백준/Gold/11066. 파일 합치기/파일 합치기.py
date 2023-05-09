import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    files = [0] + list(map(int, input().split()))
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    sum_ = [0] * (N + 1)

    for i in range(1, N + 1):
        sum_[i] = sum_[i - 1] + files[i]

    for i in range(1, N + 1):
        for x in range(1, N - i + 1):
            y = x + i
            dp[x][y] = 999999999

            for mid in range(x, y):
                dp[x][y] = min(dp[x][y], dp[x][mid] + dp[mid + 1][y] + sum_[y] - sum_[x - 1])

    print(dp[1][N])

# dp[i][j] = i번째 ~ j번째 수를 합쳤을 때
# 40 30 30 → (0 + 1) + 2 → 170
#          → 0 + (1 + 2) → 160

# dp[0][3]
# dp[0][0] + dp[1][3]
# dp[0][1] + dp[2][3]
# dp[0][2] + dp[3][3]