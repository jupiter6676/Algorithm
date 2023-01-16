N = int(input())
confs = [tuple(map(int, input().split())) for _ in range(N)]

confs.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end = confs[0][1]    # 회의 종료 시간

for i in range(1, N):
    # 다음 회의 시작 시간이, 이전 회의 종료 시간보다 늦으면
    if confs[i][0] >= end:
        cnt += 1
        end = confs[i][1]

print(cnt)