N = int(input())

res = 0
cnt = 0

while cnt != N:
    res += 1

    tmp = res
    while tmp != 0:
        if tmp % 1000 == 666:
            cnt += 1
            break
        else:
            tmp //= 10

print(res)