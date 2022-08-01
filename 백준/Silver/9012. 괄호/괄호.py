T = int(input())

for test_case in range(T):
    ps = list(input())    # Parenthesis String
    is_valid = True

    stack = list()

    for p in ps:
        if p == '(':
            stack.append(p)

        if p == ')':
            if stack:
                stack.pop()
            else:
                is_valid = False
                break

    if stack:
        is_valid = False
   
    print('YES' if is_valid else 'NO')