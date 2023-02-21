N = int(input())
seats = [0] * (N + 1)   # 모든 좌석

M = int(input())        # 고정석(vip) 개수
for _ in range(M):
    vip = int(input())
    seats[vip] = 1

dp = [1, 1, 2]
for i in range(3, N + 1):
    dp.append(dp[i - 1] + dp[i - 2])

res = 1
tmp = 0
for i in range(1, N + 1):
    if not seats[i]:
        tmp += 1
    elif tmp:
        res *= dp[tmp]
        tmp = 0
if tmp:
    res *= dp[tmp]

print(res)