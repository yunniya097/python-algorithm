# 듣보잡(1764) -> 성공
# import sys

# n, m = map(int, sys.stdin.readline().split())
# person = []
# answer = []
# num = 0

# for i in range(n):
#     nh = sys.stdin.readline()
#     person.append(nh)

# for j in range(m):
#     ns = sys.stdin.readline()
#     if ns in person:
#         answer.append(ns)
#         num += 1
    
# answer.sort()

# print(num)
# for i in range(num):
#     print(answer[i])

###############
# import sys

# n, m = map(int, input().split())
# nm = n+m
# person,answer = [], []
# num = 0

# for i in range(nm):
#     s = sys.stdin.readline().strip()
#     if s in person:
#         num += 1
#         answer.append(s)
#     else:
#         person.append(s)
    
# sorted(answer)
# print(num)
# for j in range(num):
#     print(answer[j])

#################
import sys

n, m = map(int, input().split())
nm = n+m
people = set([])
allpeople = []

for i in range(nm):
    s = sys.stdin.readline().strip()
    people.add(s)
    allpeople.append(s)

people = list(people)
num = len(allpeople)-len(people)

people.sort()
allpeople.sort()

print(num)

for i in range(len(allpeople)):
    if allpeople[i] in people:
        people.remove(allpeople[i])
    else:
        print(allpeople[i])