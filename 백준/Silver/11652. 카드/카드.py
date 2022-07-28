N = int(input())
num_cnt = dict()

for i in range(N):
    num = int(input())
    num_cnt[num] = num_cnt.get(num, 0) + 1

# 위 딕셔너리의 아이템을 value 값을 기준으로 내림차순 정렬한 후,
# key 값으로 오름차순 정렬
sorted_lst = sorted(num_cnt.items(), key=lambda x: (-x[1], x[0]))
print(sorted_lst[0][0])