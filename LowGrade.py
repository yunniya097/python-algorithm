n = int(input())
grade = []
result = []

for i in range(n):
    s, g = input().split()
    grade.append((s,int(g)))

def num(data):
    return data[1]

grade.sort(key=num)

for j in range(n):
    result.append(grade[j][0])

print(' '.join(s for s in result))