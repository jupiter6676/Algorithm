import sys
input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

res = 0
for i in range(1, W - 1):
    # i번째 블록을 기준으로, 가장 높은 왼쪽과 오른쪽 벽
    left_max = max(blocks[:i])
    right_max = max(blocks[i + 1:])

    if blocks[i] < left_max and blocks[i] < right_max:
        res += min(left_max, right_max) - blocks[i]

print(res)