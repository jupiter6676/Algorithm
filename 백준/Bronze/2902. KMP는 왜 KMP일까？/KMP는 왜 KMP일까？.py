long_str = input()

# 첫 글자 넣기
short_str = long_str[0]

for i in range(1, len(long_str) - 1):
    if long_str[i] == '-':
        short_str += long_str[i + 1]

print(short_str)