import sys
input = sys.stdin.readline

T, W = map(int, input().split())    # 떨어지는 자두 / 움직이는 횟수
trees = [0] + [int(input()) for _ in range(T)]  # T + 1

# [나무 위치][t초][이동 횟수]
dp = [[[0] * (W + 1) for _ in range(T + 1)] for _ in range(3)]

for t in range(1, T + 1):
    for w in range(W + 1):
        if trees[t] == 1:
            if w == 0:  # 이동
                dp[1][t][0] = dp[1][t - 1][0] + 1
                continue
            
            dp[1][t][w] = max(dp[1][t - 1][w], dp[2][t - 1][w - 1]) + 1
            dp[2][t][w] = max(dp[1][t - 1][w - 1], dp[2][t - 1][w])

        else:
            if w == 0:
                dp[1][t][0] = dp[1][t - 1][0]
                continue
            
            dp[1][t][w] = max(dp[1][t - 1][w], dp[2][t - 1][w - 1])
            dp[2][t][w] = max(dp[1][t - 1][w - 1], dp[2][t - 1][w]) + 1

res = 0
for i in range(1, 3):
    for j in range(1, T + 1):
        for k in range(W + 1):
            res = max(res, dp[i][j][k])
print(res)