n, k = map(int, input().split())
# 배열 A, B 입력
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
# a = [1, 2, 3, 4, 5]
# b = [6, 6, 5, 5, 5]

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
