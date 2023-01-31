import sys
input = sys.stdin.readline

N = int(input())

S = 0

for _ in range(N):
    line = input().split()

    command = line[0]
    if len(line) == 2:
        num = int(line[1])

    if command == 'add':
        S |= 1 << (20 - num)    # or
    elif command == 'remove':
        S &= ~(1 << (20 - num)) # not → and
    elif command == 'check':
        print(1 if S & (1 << (20 - num)) else 0)
    elif command == 'toggle':
        S ^= 1 << (20 - num)    # xor
    elif command == 'all':
        S = (1 << 21) - 1
    else:   # empty
        S = 0