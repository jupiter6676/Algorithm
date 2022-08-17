def func(top):
    global max_sum

    for i in range(1, N):
        max_num = 0
        flag = False

        for j in range(3):
            if flag:    break

            for k in range(2):
                if dices[i][j][k] == top:
                    bottom = dices[i][j][k]

                    if k == 0:
                        top = dices[i][j][1]
                    else:
                        top = dices[i][j][0]
                    
                    flag = True
                    break
        
        for j in range(3):
            for k in range(2):
                if not (dices[i][j][k] == top or dices[i][j][k] == bottom):
                    if dices[i][j][k] > max_num:
                        max_num = dices[i][j][k]

        max_sum += max_num

    sum_list.append(max_sum)
    
    return


N = int(input())
dices = [[] for _ in range(N)]


# i번째 주사위의 앞면, 뒷면 쌍들
for i in range(N):
    A, B, C, D, E, F = map(int, input().split())

    dices[i].append([A, F])
    dices[i].append([B, D])
    dices[i].append([C, E])

# for i in range(N):
#     print(dices[i])

sum_list = list()
for i in range(3):
    for j in range(2):
        top = dices[0][i][j]    # 위

        if j == 0:
            bottom = dices[0][i][1] # 아래
        else:
            bottom = dices[0][i][0]

        max_num = 0
        max_sum = 0

        for k in range(3):
            for l in range(2):
                if not (dices[0][k][l] == top or dices[0][k][l] == bottom):
                    if dices[0][k][l] > max_num:
                        max_num = dices[0][k][l]

        max_sum += max_num
        func(top)

# print(sum_list)
print(max(sum_list))