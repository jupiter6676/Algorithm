def hanoi(n, start, work, end):
    if n == 1:
        print(start, end)

    else:
        hanoi(n - 1, start, end, work)
        print(start, end)
        hanoi(n - 1, work, start, end)


N = int(input())

print(2 ** N - 1)

if N <= 20:
    hanoi(N, 1, 2, 3)