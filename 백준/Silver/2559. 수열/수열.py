N, K = map(int, input().split())
nums = list(map(int, input().split()))

# d의 i번째 인덱스
# → num의 i번째 숫자까지의 누적합
d = [0] * N
d[0] = nums[0]

for i in range(1, N):
    d[i] = d[i - 1] + nums[i]

max_ = d[K - 1]

for i in range(K, N):
    tmp = d[i] - d[i - K]
    max_ = max(max_, tmp)

print(max_)