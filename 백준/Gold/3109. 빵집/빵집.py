import sys
input = sys.stdin.readline

def dfs(y, x):
    global cnt

    if x == C - 1:
        cnt += 1
        return True

    # 우상, 우, 우하
    dy = [-1, 0, 1]
    dx = [1, 1, 1]

    visited[y][x] = 1

    for d in range(3):
        ny = y + dy[d]
        nx = x + dx[d]

        if not (-1 < ny < R and -1 < nx < C):
            continue

        if not visited[ny][nx] and graph[ny][nx] == '.':
            graph[ny][nx] = 'p'
            if dfs(ny, nx):
                return True

    return False


R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

cnt = 0
for i in range(R):
    if not visited[i][0] and graph[i][0] == '.':
        dfs(i, 0)

print(cnt)