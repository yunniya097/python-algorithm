n = int(input())
parts = list(map(int, input().split()))
m = int(input())
search = list(map(int, input().split()))
result = []

parts.sort()

def searching_parts(array, point, start, end):
    if start > end:
        return 'no'        
    mid = (end + start) // 2
    print(mid)

    if array[mid] == point:
        return 'yes'

    elif array[mid] > point:
        return searching_parts(array, point, start, mid-1)

    else:
        return searching_parts(array, point, mid+1, end)

for j in range(m):
    result.append(searching_parts(parts, search[j], 0, n))

print(' '.join(s for s in result))
            