# 접미사 배열(11656) --> 정답

s = input()
list = []

for i in range(len(s)):
    tail = s[i:len(s)] # baekjoon
    list.append(tail)

list.sort()

for j in range(len(list)):
    print(list[j])