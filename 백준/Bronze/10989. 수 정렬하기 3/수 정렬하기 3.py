import sys
input = sys.stdin.readline

N = int(input())
dic = dict()

for _ in range(N):
    num = int(input())
    dic[num] = dic.get(num, 0) + 1

dic = sorted(dic.items(), key=lambda x: x[0])   # key를 기준으로 오름차순 정렬

for item in dic:
    for _ in range(item[1]):
        print(item[0])