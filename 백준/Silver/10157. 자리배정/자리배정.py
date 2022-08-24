C, R = map(int, input().split())
K = int(input())

lst = [[0] * C for _ in range(R)]

flag = False
cnt = 0
last_i = 0
last_j = 0
while True:
    if flag:    break
    elif cnt == R * C:
        print(0)
        break

    # 위로 (리스트에서는 아래로)
    for i in range(last_i, R):
        if lst[i][last_j] == 1:
            i -= 1
            break

        lst[i][last_j] = 1
        cnt += 1

        if cnt == K:
            print(last_j + 1, i + 1)
            flag = True
            break

    last_i = i
    last_j += 1

    for j in range(last_j, C):
        if lst[last_i][j] == 1:
            j -= 1
            break

        lst[last_i][j] = 1
        cnt += 1

        if cnt == K:
            print(j + 1, last_i + 1)
            flag = True
            break

    last_j = j
    last_i -= 1

    for i in range(last_i, -1, -1):
        if lst[i][last_j] == 1:
            i += 1
            break

        lst[i][last_j] = 1
        cnt += 1

        if cnt == K:
            print(last_j + 1, i + 1)
            flag = True
            break

    last_i = i
    last_j -= 1

    for j in range(last_j, -1, -1):
        if lst[last_i][j] == 1:
            j += 1
            break

        lst[last_i][j] = 1
        cnt += 1

        if cnt == K:
            print(j + 1, last_i + 1)
            flag = True
            break

    last_j = j
    last_i += 1