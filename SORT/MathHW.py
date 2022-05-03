import re

n = int(input())

math = []

for i in range(n):
    hw = input()
    math.append(re.findall("\d+", hw))

math = sum(math, [])
math_0 = list(map(int, math))
math_0.sort()

for i in range(len(math_0)):
    print(math_0[i])