N = int(input())

num = 0
cnt = 0

# N번째 숫자를 찾을 때까지
while cnt != N:
    # 숫자를 1씩 계속 증가
    num += 1

    if '666' in str(num):
        cnt += 1

print(num)