N = int(input())

res = 0
for i in range(N, -1, -1):
    tmp = str(i)

    for digit in tmp:
        if not (digit == '4' or digit == '7'):
            break
    else:
        res = tmp
        break

print(res)