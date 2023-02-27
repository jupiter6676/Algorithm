import sys
from collections import deque
input = sys.stdin.readline

# 빙산 2개인지 체크
# def bfs(py, px, h):
def bfs(py, px):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited[py][px] = 1
    q.append([py, px])

    while q:
        y, x = q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if not (-1 < ny < R and -1 < nx < C):
                continue

            if not visited[ny][nx] and graph[ny][nx]:
                visited[ny][nx] = 1
                q.append([ny, nx])


# 빙산 녹이기
def melt():
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    is_all_melted = True    # 빙산이 모두 녹으면 모든 반복 종료
    this_year = [[0] * C for _ in range(R)] # 올해 녹은 빙산만 저장 (빙산이 녹아서 0이 됐을 때, 다음 빙산을 더 녹이지 않도록)

    for i in range(R):
        for j in range(C):
            if graph[i][j]:
                is_all_melted = False
                this_year[i][j] = 1

                for d in range(4):
                    ny = i + dy[d]
                    nx = j + dx[d]

                    if not (-1 < ny < R and -1 < nx < C):
                        continue

                    if graph[ny][nx] == 0 and not this_year[ny][nx]:
                        graph[i][j] -= 1
                    if graph[i][j] < 0:
                        graph[i][j] = 0

    return is_all_melted


'''main'''
R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

years = 0
while True:
    visited = [[0] * C for _ in range(R)]
    q = deque()
    cnt = 0

    for i in range(R):
        if cnt >= 2:
            break

        for j in range(C):
            if not visited[i][j] and graph[i][j]:
                bfs(i, j)
                cnt += 1

            if cnt >= 2:
                break
    
    if cnt >= 2:
        break

    if melt():
        break
    else:
        years += 1

print(years if cnt >= 2 else 0)