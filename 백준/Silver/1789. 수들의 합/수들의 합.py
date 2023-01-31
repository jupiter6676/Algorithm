S = int(input())

N = 0
sum_ = 0
while True:
    if sum_ >= S:
        break

    N += 1
    sum_ += N

res = N if sum_ == S else N - 1

print(res if N > 1 else 1)