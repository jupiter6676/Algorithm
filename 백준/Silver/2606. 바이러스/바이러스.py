V = int(input())    # 컴퓨터(정점)의 수
E = int(input())    # 간선의 수

# 인덱스 1 ~ V까지
graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)

stack = list()


def dfs(root):
    # 1번 정점을 스택에 추가, 방문 체크
    stack.append(root)
    visited[root] = True
    
    top = stack[-1]

    # 제거한 정점과 연결된 노드 탐색
    for adj in graph[top]:
        # 해당 노드를 방문하지 않았으면
        if not visited[adj]:
            dfs(adj)

    return stack.pop()


if __name__ == '__main__':
    # 인접 리스트 요소 입력
    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)    # 방향으로 하면 틀리네..

    dfs(1)
    print(sum(visited) - 1)