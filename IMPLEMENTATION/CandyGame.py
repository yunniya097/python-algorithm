n = int(input())
candies = []
candies2 = []


def find_col_candy(a, n):
    result = []
    for i in range(n):
        j = 0
        while True:

            if j == n-1:
                break

            if a[i][j] == a[i][j+1]:
                j += 1
            else:
                if i == 0:
                    if a[i+1][j] == a[i][j+1]:
                        a[i][j] = a[i+1][j]
                elif i == n-1:
                    if a[i-1][j] == a[i][j+1]:
                        a[i][j] = a[i-1][j]
                else:
                    if a[i+1][j] == a[i][j+1]:
                        a[i][j] = a[i+1][j]
                    elif a[i-1][j] == a[i][j+1]:
                        a[i][j] = a[i-1][j] 
                j += 1
            m = max(a[i].count('C'), a[i].count('P'), a[i].count('Z'), a[i].count('Y'))
            result.append(m)
            a = origin.copy.deepcopy(origin) 

        a = origin.copy.deepcopy(origin)         

    return max(result)


def find_row_candy(a, n):
    result = []
    s = []

    for i in range(n):
        j = 0
        s.clear()
        while True:
            if j == n-1:
                break

            if a[j][i] == a[j+1][i]:
                x = a[j][i]
                j += 1
            else:
                if i == 0:
                    if a[j][i+1] == a[j+1][i]:
                        a[j][i] = a[j][i+1]
                elif i == n-1:
                    if a[j][i-1] == a[j+1][i]:
                        a[j][i] = a[j][i-1]
                else:
                    if a[j][i+1] == a[j+1][i]:
                        a[j][i] = a[j][i+1]
                    elif a[j][i-1] == a[j+1][i]:
                        a[j][i] = a[j][i-1]

                x = a[j][i]
                j += 1
                
            s.append(x)
            a = origin.copy.deepcopy(origin) 

            m = max(s.count('C'), s.count('P'), s.count('Z'), s.count('Y'))
            result.append(m) 

        a = origin.copy.deepcopy(origin) 
        
    return max(result)

for i in range(n):
    candy = list(input())
    candies.append(candy)
    candies2.append

origin = candies.copy.deepcopy(candies)

row = find_row_candy(candies, n)
col = find_col_candy(candies, n)

print(max(row, col))
