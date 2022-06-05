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
if cnt != 0:
    for j in range(cnt):
        result += int(s.pop(0))
    s.append(str(result))
    string = ''.join(s)
else:
    string = ''.join(s)

print(string)

# 문자열만 들어왔을 때 0이 안붙게 하기