cnt = 0
dic = dict()

N = int(input())

for _ in range(N):
    s = input()

    if s == 'ENTER':
        dic = dict()
    
    else:
        if dic.get(s, 0) == 0:
            cnt += 1
            dic[s] = dic.get(s, 0) + 1

print(cnt)