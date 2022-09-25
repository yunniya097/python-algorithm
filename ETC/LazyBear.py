# 게으른 백곰(10025) -> 정답
n, k  = map(int, input().split())
ice = [0] * 1000000
xi = []
slider = k*2 + 1

for i in range(n):
    g, x = map(int, input().split())
    xi.append(x)
    ice[x] = g

window = sum(ice[:slider])
answer = window
xmax = max(xi)

for j in range(slider, xmax):
    window += ice[j] - ice[j-slider]
    answer = max(answer, window)

print(answer)