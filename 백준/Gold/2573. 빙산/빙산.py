import sys
from collections import deque
input = sys.stdin.readline

# 빙산 2개인지 체크
def bfs(py, px):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited[py][px] = 1
    q.append([py, px])

    while q:
        y, x = q.popleft()

        sea = 0   # [y][x] 좌표의 빙하가 총 녹을 높이 (= 바다의 수)
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if not (-1 < ny < R and -1 < nx < C):
                continue

            if not visited[ny][nx] and graph[ny][nx]:
                visited[ny][nx] = 1
                q.append([ny, nx])

            if graph[ny][nx] == 0:
                sea += 1    # 인접 바다의 수
            
        # 올해 녹은 빙산만 저장 (빙산이 녹아서 0이 됐을 때, 다음 빙산을 더 녹이지 않도록)
        melt_pos.append([y, x, sea])


# 빙산 녹이기
def melt():
    if len(melt_pos):
        is_melted = False    # 빙산이 모두 녹으면 모든 반복 종료
    else:
        is_melted = True

    for i in range(len(melt_pos)):
        y, x, sea = melt_pos[i]

        graph[y][x] -= sea

        if graph[y][x] < 0:
           graph[y][x] = 0

    return is_melted


def pprint():
    for i in range(R):
        for j in range(C):
            print(graph[i][j], end=' ')
        print()


'''main'''
R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

years = 0
is_all_melted = True
while True:
    visited = [[0] * C for _ in range(R)]
    melt_pos = list()  # 녹일 빙산의 좌표와 녹일 수치를 저장
    q = deque()

    cnt = 0 # 빙산의 개수
    for i in range(1, R - 1):
        for j in range(1, C - 1):
            if not visited[i][j] and graph[i][j]:
                bfs(i, j)
                cnt += 1

            if cnt > 1:
                break

        if cnt > 1:
            break
    
    if cnt > 1 or melt():
        break

    years += 1

print(years if cnt > 1 else 0)