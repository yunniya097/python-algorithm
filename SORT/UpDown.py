n = int(input())
result = []

for i in range(n):
    result.append(input())

result.sort(reverse=True)
print(' '.join(result))
