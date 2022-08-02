import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = list()

for _ in range(N):
    x = int(input())

    if x == 0:
        if not heap:
            print(0)
        else:
            pop = heapq.heappop(heap)
            print(pop[1])

    else:
        heapq.heappush(heap,(abs(x), x))