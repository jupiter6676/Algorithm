N = input()
dic = dict()

for num in N:
    dic[num] = dic.get(num, 0) + 1

max_v = 0
max_k = 0
for k, v in dic.items():
    if v > max_v:
        max_v = v
        max_k = k
    
    if v == max_v and not (k == '6' or k == '9'):
        max_v = v
        max_k = k

if max_k == '6' or max_k == '9':
    res = max_v - abs(dic.get('6', 0) - dic.get('9', 0)) // 2
else:
    res = max_v

print(res)