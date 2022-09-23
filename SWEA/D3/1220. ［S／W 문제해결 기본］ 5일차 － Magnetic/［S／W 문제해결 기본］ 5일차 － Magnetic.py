for t in range(1, 11):
    K = int(input())
    graph = [list(map(int, input().split())) for _ in range(K)]

    # N극이 위에 있으니까
    # 빨간 자성체를 검사해서, 파란 자성체를 만나면 교착상태 +1
    # 근데 빨간 자성체를 만나거나 0을 만나면 그대로 떨어짐

    N = 1   # N극(빨간) 자성체
    S = 2   # S극(파란) 자성체

    total = 0

    # 열부터 탐색
    for j in range(K):
        tmp_cnt = 0

        for i in range(K):
            if graph[i][j] == N and tmp_cnt == 0:
                tmp_cnt = 1
            
            if tmp_cnt == 1 and graph[i][j] == S:
                total += tmp_cnt
                tmp_cnt = 0

    print(f'#{t} {total}')