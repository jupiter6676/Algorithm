import sys
input = sys.stdin.readline

T = 1
while True:
    N = int(input())

    if N == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * 3 for _ in range(N)]

    dp[0][0] = 99999999
    dp[0][1] = graph[0][1]
    dp[0][2] = dp[0][1] + graph[0][2]
    
    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + graph[i][0]
        dp[i][1] = min(dp[i][0], min(dp[i - 1])) + graph[i][1]
        dp[i][2] = min(dp[i][1], dp[i - 1][1], dp[i - 1][2]) + graph[i][2]

    print(f'{T}. {dp[N - 1][1]}')
    T += 1