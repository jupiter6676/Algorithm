def solution():
    if len(seq) == M:
        if res.get(tuple(seq), 0) == 0:
            res[tuple(seq)] = 1 # 리스트 끝에 iterable의 모든 항목 넣기
        return

    for i in range(len(lst)):
        if not visited[i]:
            seq.append(lst[i])
            visited[i] = True
            solution()

            seq.pop()
            visited[i] = False


'''main'''
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [False] * N   # lst[i] ↔ visited[i]
seq = list()

# 키로 seq의 튜플
res = dict()

solution()

for seq in res.keys():
    print(*seq)