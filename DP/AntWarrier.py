n = int(input())
food = list(map(int, input().split()))
result = 0

d = [0] * 101

for i in range(2, n):
    d[0] = food[0]
    d[1] = food[1]
    d[i] = food[i] + food[i-2]

    if d[i] >= d[i-1]:
        result = d[i]

    else:
        result = d[i-1]   
    
print(result)


