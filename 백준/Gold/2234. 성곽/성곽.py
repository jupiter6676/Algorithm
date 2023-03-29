import sys
from collections import deque
input = sys.stdin.readline

def bfs(py, px, room_cnt):
    visited[py][px] = room_cnt
    q.append([py, px])
    room_size = 1    # 방 넓이

    while q:
        y, x = q.popleft()

        for d in range(4):
            if (graph[y][x] & walls[d] == walls[d]):
                continue

            ny = y + dy[d]
            nx = x + dx[d]

            if not (-1 < ny < R and -1 < nx < C):
                continue
            
            if not visited[ny][nx]:
                visited[ny][nx] = room_cnt
                q.append([ny, nx])
                room_size += 1

    return room_size    

'''main'''
C, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

q = deque()
dy = [1, 0, -1, 0]  # SENW
dx = [0, 1, 0, -1]  # SENW
walls = [8, 4, 2, 1]

rooms = list()  # 각 방의 넓이

room_cnt = 0
max_room_size = 0
for i in range(R):
    for j in range(C):
        if not visited[i][j]:
            room_cnt += 1
            max_room_size = max(max_room_size, bfs(i, j, room_cnt))

print(room_cnt)
print(max_room_size)

for i in range(R):
    for j in range(C):
        for d in range(4):
            if (graph[i][j] & walls[d] == walls[d]):
                visited = [[0] * C for _ in range(R)]
                graph[i][j] -= walls[d]
                max_room_size = max(max_room_size, bfs(i, j, 1))
                graph[i][j] += walls[d]

print(max_room_size)