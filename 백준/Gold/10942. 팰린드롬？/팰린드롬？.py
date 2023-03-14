import sys
input = sys.stdin.readline

N = int(input())
nums = [0] + list(map(int, input().split()))
M = int(input())

# dp[i][j]: i번째 수 ~ j번째 수가 팰린드롬인가
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][i] = 1

    if nums[i - 1] == nums[i]:
        dp[i - 1][i] = 1    # 11, 22 이런 것도 팰린드롬

for i in range(N, 0, -1):
    for j in range(N, i - 1, -1):
        if nums[i] != nums[j]:
            dp[i][j] = 0
        
        else:
            if j + 1 <= N:
                dp[i - 1][j + 1] = dp[i][j]

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S][E])