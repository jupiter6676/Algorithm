T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    boxes = [list(map(int, input().split())) for _ in range(N)]
    dist = [0] * M

    tmp = 0
    # 0행부터 M행까지
    for j in range(M):
        tmp = 0
        # 박스를 아래로 떨어뜨리기
        # 바닥에서 위로 거슬러 올라가기
        for i in range(N - 1, -1, -1):
            if boxes[i][j] == 0:
                tmp += 1
            else:
                dist[j] += tmp

    print(sum(dist))