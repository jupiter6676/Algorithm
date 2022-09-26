T = int(input())
for t in range(1, T + 1):
    graph = [list(map(int, input().split())) for _ in range(9)]

    is_valid = True

    # 가로 & 세로
    for i in range(9):
        col = list()

        for j in range(9):
            row = graph[i]
            col.append(graph[j][i])

        if len(set(row)) < 9 or len(set(col)) < 9:
            is_valid = False
            break
    
    # 3 X 3
    if is_valid:
        for i in range(9):
            for j in range(9):
                if (i == 0 or i == 3 or i == 6) and (j == 0 or j == 3 or j == 6):
                    submatrix = list()
                    for y in range(3):
                        for x in range(3):
                            submatrix.append(graph[i + y][j + x])

                    if len(set(submatrix)) < 9:
                        is_valid = False
                        break
    
    print(f'#{t}', end=' ')
    print(1 if is_valid else 0)