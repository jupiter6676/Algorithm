import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
q = deque()
seq = list()

for i in range(1, N + 1):
    q.append(i)

while q:
    for i in range(K - 1):
        pop = q.popleft()
        q.append(pop)

    seq.append(q.popleft())

print('<', end='')
print(*seq, sep=', ', end='')
print('>')