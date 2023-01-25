N, K = map(int, input().split())
seq = list(map(int, input().split()))  # 전자기기 사용 순서

plugs = [0] * (K + 1)

tmp_sum = 0
res = 0

for i in range(K):
    if tmp_sum < N:
        if not plugs[seq[i]]:
            tmp_sum += 1

        plugs[seq[i]] = 1

    else:
        if not plugs[seq[i]]:
            tmp_list = list()

            for j in range(i, K):
                if plugs[seq[j]] and not seq[j] in tmp_list:
                    tmp_list.append(seq[j])
                if len(tmp_list) == N:
                    break
            
            for j in range(K):
                if plugs[seq[j]] and not seq[j] in tmp_list:
                    plugs[seq[j]] = 0
                    break

            else:
                plugs[tmp_list[-1]] = 0

            res += 1
            plugs[seq[i]] = 1

print(res)