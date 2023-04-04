import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    # 원숭이
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # 말
    hy = [-2, -2, -1, -1, 1, 1, 2, 2]
    hx = [-1, 1, -2, 2, -2, 2, -1, 1]

    q = deque()

    q.append([K, 0, 0])
    visited[K][0][0] = 1

    while q:
        k, y, x = q.popleft()

        if y == H - 1 and x == W - 1:
            return

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if not (-1 < ny < H and -1 < nx < W):
                continue

            if not graph[ny][nx]:
                if not visited[k][ny][nx]:
                    visited[k][ny][nx] = visited[k][y][x] + 1
                    q.append([k, ny, nx])

        if k:
            for h in range(8):
                ny = y + hy[h]
                nx = x + hx[h]

                if not (-1 < ny < H and -1 < nx < W):
                    continue

                if not graph[ny][nx]:
                    if not visited[k - 1][ny][nx]:
                        visited[k - 1][ny][nx] = visited[k][y][x] + 1
                        q.append([k - 1, ny, nx])

K = int(input())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]
visited = [[[0] * W for _ in range(H)] for _ in range(K + 1)]   # 말의 능력 사용 가능 횟수

bfs()

MAX = 99999999
res = MAX
for k in range(K + 1):
    if visited[k][H - 1][W - 1]:
        res = min(res, visited[k][H - 1][W - 1])

print(res - 1 if res != MAX else -1)