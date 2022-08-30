import sys
input = sys.stdin.readline

N = int(input())
graph = [[0] * 1001 for _ in range(1001)]
area = [0] * (N + 1)

for p in range(1, N + 1):
    x1, y1, w, h = map(int, input().split())

    x2 = x1 + w
    y2 = y1 + h

    for i in range(y1, y2):
        for j in range(x1, x2):
            if graph[i][j] != p:
                area[graph[i][j]] -= 1
            
            graph[i][j] = p
            area[graph[i][j]] += 1
            
for i in range(1, len(area)):
    print(area[i])