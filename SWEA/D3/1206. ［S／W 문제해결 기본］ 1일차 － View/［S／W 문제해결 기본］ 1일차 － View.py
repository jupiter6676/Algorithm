for t in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))   # N + 4의 크기

    cnt = 0

    for i in range(2, len(lst) - 2):
        tmp = lst[i]

        while True:
            if lst[i - 2] < tmp and lst[i - 1] < tmp and lst[i + 1] < tmp and lst[i + 2] < tmp:
                cnt += 1
                tmp -= 1
            else:
                break

    print(f'#{t} {cnt}')