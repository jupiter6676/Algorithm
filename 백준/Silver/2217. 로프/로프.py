N = int(input())
nums = list()

for _ in range(N):
    nums.append(int(input()))

nums.sort(reverse=True) # 내림차순 정렬

max_res = 0
for _ in range(N):
    max_res = max(max_res, nums[-1] * len(nums))
    nums.pop()

print(max_res)