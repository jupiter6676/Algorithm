T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split()) # 손님 N명, M초에 K개의 붕어빵
    customers = list(map(int, input().split())) # 손님 도착 시각

    is_possible = True
    max_sec = max(customers) # 가장 늦게 입장했을 때의 시간

    ch = [0] * (max_sec + 1)   # 몇 초에 손님이 도착했는지 체크
    for i in range(N):
        ch[customers[i]] = 1

    bread = 0
    for sec in range(max_sec + 1):
        # M초가 지나면 K개의 붕어빵 굽기
        if sec > 0 and sec % M == 0:
            bread += K

        # 손님이 도착했을 때
        if ch[sec]:
            # 붕어빵이 없으면 Impossible
            if bread <= 0:
                is_possible = False
            # 붕어빵이 있으면 하나 판매
            else:
                bread -= 1

    print(f'#{t}', end=' ')
    print('Possible' if is_possible else 'Impossible')