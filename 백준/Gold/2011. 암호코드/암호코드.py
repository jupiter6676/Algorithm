code = [-1] + list(map(int, input()))
N = len(code) - 1   # 입력된 수의 개수

dp = [0] * (N + 1)  # dp[i]: i번째 수 까지의 경우의 수
dp[0] = 1

for i in range(1, N + 1):
    if 1 <= code[i] <= 9:
        dp[i] = (dp[i - 1] + dp[i]) % 1000000

    tmp = code[i - 1] * 10 + code[i]
    if 10 <= tmp <= 26:
        dp[i] = (dp[i - 2] + dp[i]) % 1000000

print(dp[N])