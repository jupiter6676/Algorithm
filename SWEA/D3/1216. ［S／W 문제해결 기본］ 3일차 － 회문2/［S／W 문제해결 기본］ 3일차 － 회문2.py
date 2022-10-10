# 시계방향으로 90도 회전
def rotate(matrix):
    rotated = [[0] * 100 for _ in range(100)]

    for i in range(100):
        for j in range(100):
            rotated[i][j] = matrix[100 - j - 1][i]

    return rotated


'''main'''
for _ in range(1, 11):
    t = int(input())

    graph = [list(input()) for _ in range(100)]
    max_len = 0

    # N은 회문의 길이
    for N in range(100, 0, -1):
        # 1. 가로
        for i in range(100):
            str_ = ''

            for j in range(100 - (N - 1)):
                # 회문의 길이(N)만큼 회문 만들기
                str_ = ''.join(graph[i][j : j + N])

                if str_ == str_[::-1]:
                    # print(str_)
                    max_len = max(max_len, N)

    rotated_graph = rotate(graph)
    for N in range(100, 0, -1):
        # 2. 세로
        for i in range(100):
            str_ = ''

            for j in range(100 - (N - 1)):
                # 회문의 길이(N)만큼 회문 만들기
                str_ = ''.join(rotated_graph[i][j : j + N])

                if str_ == str_[::-1]:
                    # print(str_)
                    max_len = max(max_len, N)

    print(f'#{t} {max_len}')