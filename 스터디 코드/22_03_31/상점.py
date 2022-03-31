url = "https://euleroj.io/problemset/viewer/2113"

c = int(input())
n = int(input())
a = [0]
a[1:] = list(map(int, input().split()))

isOk = False
for i in range(1,n):
    for j in range(i+1, n+1):
        if a[i] + a[j] == c:
            print(i, j)
            isOk = True
            break
    if isOk == True:
        break