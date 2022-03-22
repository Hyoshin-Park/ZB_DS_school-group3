#https://codeup.kr/problem.php?id=3008

small = []
for _ in range(9):
    a = int(input())
    small.append(a)
ss = sum(small)
ss = ss - 100
for i in range(8):
    for j in range(i+1,9):
        if small[i] + small[j] == ss:
            q = small[i]
            p = small[j]


small.remove(p)
small.remove(q)
small.sort()
for r in small:
    print(r)