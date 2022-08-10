import sys
input = sys.stdin.readline

V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
stack = list()

connected_cnt = 0

def dfs(start):
    global connected_cnt

    stack.append(start)
    visited[start] = True

    while stack:
        pop = stack.pop()

        for adj in graph[pop]:
            if not visited[adj]:
                stack.append(adj)
                visited[adj] = True

    connected_cnt += 1

    return


# 그래프 정보 입력
for _ in range(E):
    v1, v2 =  map(int, input().split())

    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, V + 1):
    if not visited[i]:
        dfs(i)

print(connected_cnt)