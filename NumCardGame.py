n, m = map(int, input().split())
result = 0

card = [list(map(int, input().split())) for _ in range(n)]
min_num = min(card)

if(min_num > result):
    result = min_num
else:
    result = result
print(result)