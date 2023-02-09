from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    # 상자 위, 상자 아래 / 상하좌우
    dz = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dx = [0, 0, 0, 0, -1, 1]

    while q:
        z, y, x = q.popleft()

        for d in range(6):
            nz = z + dz[d]
            ny = y + dy[d]
            nx = x + dx[d]

            if not (-1 < nz < H and -1 < ny < R and -1 < nx < C):
                continue

            if boxes[nz][ny][nx] == 0:
                q.append([nz, ny, nx])
                boxes[nz][ny][nx] = boxes[z][y][x] + 1


C, R, H = map(int, input().split())

# 3차원 리스트
boxes = [
    [list(map(int, input().split())) for _ in range(R)] for _ in range(H)
]

visited = [[[0] * C for _ in range(R)] for _ in range(H)]
q = deque()

for z in range(H):
    for y in range(R):
        for x in range(C):
            if boxes[z][y][x] == 1:
                q.append([z, y, x])

bfs()

res = 0
is_possible = True
for box in boxes:
    for row in box:
        for t in row:
            if t == 0:
                res = 0
                break

            res = max(res, t)
        else:
            continue
        break
    else:
        continue
    break

print(res - 1)