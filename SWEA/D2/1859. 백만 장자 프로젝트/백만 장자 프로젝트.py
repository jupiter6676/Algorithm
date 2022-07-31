T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    # 매매가 정보 입력
    price = list(map(float, input().split()))

    max_price = price[N - 1]    # 마지막 원소
    max_profit = 0  # result

    for i in range(N - 1, -1, -1):   # (N - 1) ~ 1
        if price[i] < max_price:
                max_profit += max_price - price[i]

        # 현재 i번째, 이전 i - 1번째
        # i - 1번째 원소가 현재보다 더 크고, max_price보다 더 크면
        # i - 1번째 원소가 첫 번째 원소가 아닐 때 max_price 값 갱신
        if price[i - 1] > price[i] and price[i - 1] > max_price:
            if i - 1 != 0:
                max_price = price[i - 1]

    print(f'#{test_case} {int(max_profit)}')