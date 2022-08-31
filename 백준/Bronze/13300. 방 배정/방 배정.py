stu = [[0] * 6 for _ in range(2)]

N, K = map(int, input().split())

for _ in range(N):
    gender, grade = map(int, input().split())

    stu[gender][grade - 1] += 1

cnt = 0
for i in range(2):
    for j in range(6):
        if stu[i][j] != 0:
            if stu[i][j] > K:
                cnt += stu[i][j] // K if stu[i][j] % K == 0 else stu[i][j] // K + 1
            else:
                cnt += 1

print(cnt)