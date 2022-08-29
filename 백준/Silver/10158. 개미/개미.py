w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

NE = 1  # 오른쪽 위 45도 방향
SW = 0  # 왼쪽 아래 45도 방향

x_cnt = (p + t) // w    # x좌표 왕복 횟수
y_cnt = (q + t) // h    # y좌표 왕복 횟수

# x좌표 왕복 횟수가 짝수
# → 0에서 w로 오는 변곡점
if x_cnt % 2 == 0:
    p = (p + t) % w

# x좌표 왕복 횟수가 홀수
# → w에서 0으로 오는 변곡점
else:
    p = w - (p + t) % w

# y좌표
if y_cnt % 2 == 0:
    q = (q + t) % h
else:
    q = h - (q + t) % h

print(p, q)