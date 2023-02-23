N = int(input())
packs = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)  # dp[i]: 카드 i개 → 최대 금액

for i in range(1, N + 1):
    tmp_list = []

    for j in range(1, i + 1):
        if i % j == 0:
            tmp_list.append(packs[j] * (i // j))
        elif i > j:
            tmp_list.append(packs[j] + dp[i - j])

    # print(tmp_list)
    dp[j] = max(tmp_list)

# print(dp)
print(dp[N])