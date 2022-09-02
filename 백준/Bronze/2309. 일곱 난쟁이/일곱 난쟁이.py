total = 0
lst = list()

for _ in range(9):
    n = int(input())

    total += n
    lst.append(n)

lst.sort()

i = 0
flag = False

while True:
    for j in range(i + 1, 9):
        if total - lst[i] - lst[j] == 100:
            flag = True
            break

    if flag:    break

    i += 1

for k in range(9):
    if not (k == i or k == j):
        print(lst[k])