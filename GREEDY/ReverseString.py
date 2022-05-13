# 문자열 뒤집기
import sys

s = list(map(int, sys.stdin.readline().rstrip()))
cnt_0, cnt_1 = 0, 0
# zero, one = []

# 처음 시작하는게 0인지 1인지 파악한 뒤 해당하는 값의 cnt += 1
if s[0] == 0:
    cnt_0 += 1
else:
    cnt_1 += 1

for i in range(len(s)-1):
    if s[i] == 0 and s[i] != s[i+1]:
            cnt_1 += 1

    elif s[i] == 1 and s[i] != s[i+1]:
            cnt_0 += 1

# 더 적은 횟수 출력
if cnt_0 >= cnt_1:
    print(cnt_1)
else:
    print(cnt_0)
