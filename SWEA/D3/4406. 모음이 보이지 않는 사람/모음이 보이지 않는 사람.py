T = int(input())

for tc in range(1, T + 1):
    S = input()
    res = ''

    for ch in S:
        if ch not in 'aeiou':
            res += ch

    print(f'#{tc} {res}')