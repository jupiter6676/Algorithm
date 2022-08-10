import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)

# 좌상, 상, 우상, 우, 우하, 하, 좌하, 좌
dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]

def dfs(y, x, cnt):
    visited[y][x] = True
    graph[y][x] = cnt

    for d in range(8):
        ny = y + dy[d]
        nx = x + dx[d]

        if not (-1 < ny < h and -1 < nx < w):
            continue

        if graph[ny][nx] == 1 and not visited[ny][nx]:
            graph[ny][nx] = cnt
            visited[ny][nx] = True

            dfs(ny, nx, cnt)


while True:
    w, h = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range (h)]
    
    if w == 0 and h == 0:
        break

    visited = [[False] * w for _ in range(h)]
    island_cnt = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                island_cnt += 1
                dfs(i, j, island_cnt)

    print(island_cnt)