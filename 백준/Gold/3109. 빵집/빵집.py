import sys
input = sys.stdin.readline

def dfs(y, x):
    global is_arrived

    # 우상, 우, 우하
    dy = [-1, 0, 1]
    dx = [1, 1, 1]

    visited[y][x] = 1

    for d in range(3):
        if is_arrived:
            return

        ny = y + dy[d]
        nx = x + dx[d]

        if not (-1 < ny < R and -1 < nx < C):
            continue

        if not visited[ny][nx] and graph[ny][nx] == '.':
            graph[ny][nx] = 'p'

            if nx == C - 1:
                is_arrived = True

            dfs(ny, nx)


R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

for i in range(R):
    if not visited[i][0] and graph[i][0] == '.':
        is_arrived = False
        dfs(i, 0)

cnt = 0
for i in range(R):
    if graph[i][C - 1] == 'p':
        cnt += 1

print(cnt)