# 프린터 큐(1966)
testcase = int(input())
ans = []

for i in range(testcase):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))

    order = 0

    if n == 1:
        ans.append(1)

    else:
        doc = imp[m]
        cnt = imp.count(doc)
        doc_idx = m
        
        if cnt == 1: # 찾는 문서랑 중요도가 같은게 없을 때
            while True:
                if max(imp) == imp[0]:
                    order += 1
                    if imp[0] == doc:
                        break
                    imp.pop(0)
                else:
                    q = imp.pop(0)
                    imp.append(q)

        else: # 찾는 문서랑 중요도가 같은게 있을 때
            while True:
                if len(imp) == 1:
                    order += 1
                    break
                else:
                    max_i = max(imp)
                    if max(imp)!= doc:
                        if max(imp) == imp[0]:
                            order += 1
                            imp.pop(0)
                        else:
                            q = imp.pop(0)
                            imp.append(q)
                    else:
                        if doc_idx % n == m+1:
                            order += 1
                            break
                        else:
                            if max(imp) == imp[0]:
                                order += 1
                                imp.pop(0)
                            else:
                                q = imp.pop(0)
                                imp.append(q)
                doc_idx += 1           
                
            
        ans.append(order)

for j in range(len(ans)):
    print(ans[j])