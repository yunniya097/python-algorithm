n, m, k = map(int, input().split())
cnt = k
result = 0
num_list = list(map(int, input().split()))

# 정렬
num_list.sort() 
print(num_list)

# 첫 번째로 큰 수, 두 번째로 큰 수
f_num = num_list[n-1]
s_num = num_list[n-2]
print(s_num)

for j in range(m):
    if(cnt > 0):
        result += f_num
        cnt -= 1
        print(result)
    else:
        result += s_num
        cnt = k
        print(result)

print(result)