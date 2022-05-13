# 문자열 재정렬
import sys
s = list(sys.stdin.readline().rstrip())
s.sort()
cnt, result = 0, 0

for i in range(len(s)):
    if ord(s[i]) < 65:
        cnt += 1
    else:
        break

for j in range(cnt):
    result += int(s.pop(0))

s.append(str(result))
string = ''.join(s)
print(string)