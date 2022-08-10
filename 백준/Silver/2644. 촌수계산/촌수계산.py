''' 변수 선언 '''
V = int(input())
a, b = map(int, input().split()) # 촌수 계산 대상
E = int(input())

graph = [[] for _ in range(V + 1)]
visited = [0] * (V + 1)
dist = [0] * (V + 1)


''' dfs 함수 '''
def dfs(start, end):
    global dist

    visited[start] = 1

    if start == end:
        return dist

    for adj in graph[start]:
        if not visited[adj]:
            visited[adj] = 1
            dist[adj] = dist[start] + 1
            
            dfs(adj, end)
    
    return


''' 메인 '''
# 그래프 정보 입력
for _ in range(E):
    v1, v2 =  map(int, input().split())

    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(a, b)
print(dist[b] if dist[b] else -1)