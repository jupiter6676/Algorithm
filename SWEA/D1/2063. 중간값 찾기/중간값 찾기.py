N = int(input())    # N은 항상 홀수
lst = list(map(int, input().split()))

lst.sort()

print(lst[N // 2])