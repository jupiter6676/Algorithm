T = int(input())
for test_case in range(1, T + 1):
    s = input()
    mirrored_s = ''

    for ch in s[::-1]:
        if ch == 'b':
            mirrored_s += 'd'
        elif ch == 'd':
            mirrored_s += 'b'
        elif ch == 'p':
            mirrored_s += 'q'
        else:
            mirrored_s += 'p'

    print(f'#{test_case} {mirrored_s}')