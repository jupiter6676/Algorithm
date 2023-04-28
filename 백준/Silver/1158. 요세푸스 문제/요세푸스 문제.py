import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = [i for i in range(N + 1)]
visited = [0] * (N + 1)
seq = list()

cnt = 0
i = 0
flag = 0
while True:
    if flag == N:
        break

    if not visited[i]:
        if cnt > 0 and cnt % K == 0:
            seq.append(nums[i])
            visited[i] = 1
            flag += 1

        cnt += 1

    i %= N
    i += 1

print('<', end='')
print(*seq, sep=', ', end='')
print('>')