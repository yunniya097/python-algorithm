n, m = map(int, input().split())
result = 0

for i in range(n):
    card = list(map(int, input().split()))
    min_num = min(card)
    
    if(min_num > result):
        result = min_num

print(result)