import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T + 1):
    ox = input()
    total_score = 0
    plus_score = 1

    for curr in ox:
        if curr == 'O':
            total_score += plus_score
            plus_score += 1
            continue

        plus_score = 1

    print(total_score)