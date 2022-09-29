T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    mono_lst = list()

    for i in range(N - 1):
        for j in range(i + 1, N):
            num = lst[i] * lst[j]
            is_mono = True  # monotic

            tmp = num

            # 1의 자리 수
            digit = tmp % 10
            tmp //= 10

            while tmp > 0:
                # 맨 오른쪽 끝 수(digit)와 바로 왼쪽 수(tmp % 10, 10의 자리 수 부터) 비교
                if tmp % 10 > digit:
                    is_mono = False
                    break

                digit = tmp % 10
                tmp //= 10

            if is_mono:
                mono_lst.append(num)

    print(f'#{t}', end=' ')
    if mono_lst:
        print(max(mono_lst))
    else:
        print(-1)