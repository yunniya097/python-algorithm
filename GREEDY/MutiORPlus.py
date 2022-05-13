# 곱하기 또는 더하기
import sys

s = list(map(int, sys.stdin.readline().rstrip())) # sys.stdin.readline() -> 입력 / rstrip() -> 문자열의 맨 마지막 공백을 지워주는 함수
result = s[0]
for i in range(1, len(s)):
    if result == 0:
        result += s[i]
    elif s[i] == 0:
        result += s[i]
    else:
        result *= s[i]

print(result)