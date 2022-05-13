# 럭키 스트레이트
import sys

n = list(map(int, sys.stdin.readline().rstrip()))
m = int(len(n)/2)

r, l = 0, 0

# 기준점보다 오른쪽에 있으면 r에 더하기
for i in range(m):
    r += n[i]

# 기준점보다 왼쪽에 있으면 l에 더하기
for j in range(m, len(n)):
    l += n[j]
    
# 비교해서 출력
if r == l:
    print("LUCKY")
else:
    print("READY")
