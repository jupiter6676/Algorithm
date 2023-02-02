N = int(input())
dists = list(map(int, input().split()))
prices = list(map(int, input().split()))    # 0 ~ (N - 1)

dists.append(0)

res = 0
tmp_dist = dists[0]    # 주유소 가격이 오르면 계속 증가, 내리면 초기화
tmp_price = prices[0]

for i in range(1, N):
    if tmp_price < prices[i]:
        tmp_dist += dists[i]

    else: 
        res += tmp_price * tmp_dist
        tmp_price = prices[i]
        tmp_dist = dists[i]

print(res)