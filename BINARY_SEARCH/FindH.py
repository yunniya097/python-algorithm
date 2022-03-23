import math

n, m = map(int, input().split())
ddeok = (list(map(int, input().split())))
result = 0

ddeok.sort()

h = sum(ddeok)//n

def binary_search(array, point, start, end):
    while start <= end:
        mid = math.ceil((start + end) / 2)
        
        if array[mid] == point:
            return mid
		# 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > point:
            end = mid - 1
		# 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1


sta = binary_search(ddeok, h, 0, n)

while True:
    n -= sta
    for i in range(n):
        result += ddeok[sta+i]
        
    if result == m:
        break
    elif result > m:
        sta = binary_search(ddeok, h+1, 0, n)
    else:
        sta = binary_search(ddeok, h-1, 0, n)

print(result)