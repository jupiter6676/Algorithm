import sys
input = sys.stdin.readline

N, L = map(int, input().split())        # 물이 새는 곳의 개수, 테이프의 길이
water = list(map(int, input().split())) # 물 새는 곳의 위치
cnt = 0

water.sort()

tmp_len = 0
for i in range(N):
    if i < N - 1:
        dist = water[i + 1] - water[i]  # 현재 위치 ~ 다음 위치까지의 거리
    else:
        dist = 1    # 가장 마지막 위치인 경우, 거리는 1

    if tmp_len + dist < L:
        tmp_len += dist  # 테이프를 다음 이동 거리만큼 사용
    else:
        cnt += 1
        tmp_len = 0

if tmp_len > 0:
    cnt += 1

print(cnt)