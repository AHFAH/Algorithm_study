a = int(input())


for i in range(a):
    n, m = map(int, input().split())
    doc = list(map(int, input().split()))
    result = 1

    while doc:
        if doc[0] < max(doc):
            doc.append(doc.pop(0))

        else:
            if m == 0:
                break

            doc.pop(0)
            result += 1

        if m == 0:
            m = len(doc) - 1
        else:
            m -= 1

    print(result)



    # 다시 풀어보기
