from collections import deque

N, K = map(int, input().split())
size = N if N > K else K

graph = [0] * (size + 2) # 한 칸 넘었다가 다시 뒤로 돌아오는 경우도 O
graph[N] = 1
q = deque()

dx = [1, -1, 2]

if N == K:
    print(0)

else:
    q.append(N)
    while q:
        x = q.popleft()
        
        for d in range(3):
            if dx[d] != 2:
                nx = x + dx[d]
            else:
                nx = x * 2

            if not (-1 < nx < size + 2):
                continue
            
            if graph[nx] == 0:
                q.append(nx)
                graph[nx] = graph[x] + 1

    print(graph[K] - 1)