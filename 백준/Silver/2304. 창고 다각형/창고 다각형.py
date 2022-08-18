N = int(input())
pillar = [0] * 1001 # idx: 기둥 위치, val: 기둥 높이

first = 999999
last = 0
max_height = 0

for _ in range(N):
    L, H = map(int, input().split())
    pillar[L] = H

    if L > last:
        last = L
    if L < first:
        first = L
    
    if H > max_height:
        max_height = H


stack = list()
stack.append(pillar[first])

is_asc = True
for i in range(first + 1, last + 1):
    if is_asc:
        if stack[-1] < pillar[i]:
            stack.append(pillar[i])

        else:
            stack.append(stack[-1])

        if pillar[i] == max_height:
            is_asc = False
            break

if not is_asc and i != last:
    # 맨 끝 (가장 낮은 곳)의 높이 추가
    stack.append(pillar[last])

    # 맨 끝 한 칸 앞에서부터 시작,
    # 중단된 부분(최고점)의 한 칸 뒤까지 반복
    for j in range(last - 1, i, -1):
        if stack[-1] < pillar[j]:
            stack.append(pillar[j])

        else:
            stack.append(stack[-1])

        # print(stack)

print(sum(stack))