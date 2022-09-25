# 기타줄_1049
n, m = map(int, input().split())
result = 0

package, unit = [], []

for i in range(m):
    p, u = map(int, input().split())
    package.append(p)
    unit.append(u)

p_min = min(package)
u_min = min(unit)

if n <= 6:
    result = min(p_min, u_min * n)
else:
    s = n // 6
    r = n % 6
    result = min(s * p_min + r * u_min, (s+1) * p_min, n * u_min)

print(result)

# divmod() => 몫 나머지 한 번에