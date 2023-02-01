import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewels.sort(key=lambda x: (x[0], -x[1]))    # 무게 오름차순, 가격 내림차순
bags.sort()

q = list()
res = 0
for i in range(K):
    while jewels and jewels[0][0] <= bags[i]:
        heapq.heappush(q, -jewels[0][1])
        heapq.heappop(jewels)

    if q:
        res -= heapq.heappop(q)

print(res)
