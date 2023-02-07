import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]   # 0일 ~ N - 1일까지 상담, 퇴사일은 N일
dp = [0] * (N + 1)  # 해당 상담을 했을 때의 누적 금액

for i in range(N - 1, -1, -1):
    end = i + lst[i][0]

    if end > N:
        dp[i] = dp[i + 1]
        
    else:
        dp[i] = max(dp[i + 1], dp[end] + lst[i][1])

print(dp[0])