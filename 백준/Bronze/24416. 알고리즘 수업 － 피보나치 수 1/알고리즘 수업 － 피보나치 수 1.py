# DP
def fibo_dp(n):
    global cnt_dp
    dp = [0, 1, 1]

    for i in range(3, n + 1):
        cnt_dp += 1
        dp.append(dp[i - 1] + dp[i - 2])

    return dp[n]


'''main'''
N = int(input())
cnt_dp = 0

print(fibo_dp(N), cnt_dp)