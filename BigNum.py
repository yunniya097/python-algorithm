n, m, k = map(int, input().split())
cnt = k
result = 0
num_list = list(map(int, input().split()))

# 정렬
num_list.sort() 

# 첫 번째로 큰 수, 두 번째로 큰 수
f_num = num_list[n-1]
s_num = num_list[n-2]

for j in range(m):
    if(cnt > 0):
        result += f_num
        cnt -= 1

    else:
        result += s_num
        cnt = k

print(result)