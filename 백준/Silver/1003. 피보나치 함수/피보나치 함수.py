def fibo(n):
    for i in range(2, n + 1):
        tmp_list = list()
        tmp_list.append(dp[i - 1][0] + dp[i - 2][0])
        tmp_list.append(dp[i - 1][1] + dp[i - 2][1])

        dp.append(tmp_list)


T = int(input())

for t in range(T):
    N = int(input())
    dp = [[1, 0], [0, 1]]   # 0, 1일 때의 0과 1의 개수
    cnt_list = [0, 0]

    fibo(N)
    print(*dp[N])