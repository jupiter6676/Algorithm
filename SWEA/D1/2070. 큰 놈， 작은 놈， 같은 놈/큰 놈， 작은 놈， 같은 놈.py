T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    res = '>' if a > b else '<' if a < b else '='

    print(f'#{test_case} {res}')