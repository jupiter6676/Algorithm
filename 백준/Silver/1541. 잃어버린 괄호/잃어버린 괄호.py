# -를 기준으로 식 나누기
lst = input().split('-')

# +가 있는 식 계산해서 새 리스트 만들기
nums = list()
for elem in lst:
    nums.append(sum(map(int, elem.split('+'))))

res = nums[0]   # 첫 번째 수는 빼기 X
for i in range(1, len(nums)):
    res -= nums[i]

print(res)