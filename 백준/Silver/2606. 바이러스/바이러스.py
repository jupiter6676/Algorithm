from collections import deque


V = int(input())    # 컴퓨터(정점)의 수
E = int(input())    # 간선의 수

# 인덱스 1 ~ V까지
graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)

queue = deque()

def bfs(root):
    queue.append(root)
    visited[root] = True

    while queue:
        pop = queue.popleft()

        for adj in graph[pop]:
            if not visited[adj]:
                queue.append(adj)
                visited[adj] = True

    cnt = 0
    for i in range(2, V + 1):
        if visited[i]:
            cnt += 1

    return cnt

if __name__ == '__main__':
    # 인접 리스트 요소 입력
    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    print(bfs(1))