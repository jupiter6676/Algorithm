# 총 10개의 테스트 케이스
for test_case in range(1, 11):
    # 입력 1. 원본 암호문의 길이
    N = int(input())
    # 입력 2. 원본 암호문
    code = list(input().split())
    # 입력 3. 명령어의 개수
    M = int(input())
    # 입력 4. 명령어
    command = input().split()

    i = 1
    while i < len(command):
        if command[i - 1] == 'I':
            insert_idx = int(command[i])
            insert_cnt = int(command[i + 1])
            i += 2

        for j in range(insert_cnt):
            code.insert(insert_idx, command[i])
            i += 1
            insert_idx += 1

        i += 1

    #print(code[:10])
    print(f'#{test_case}', end=' ')
    for k in range(10):
        print(code[k], end=' ')
    print()