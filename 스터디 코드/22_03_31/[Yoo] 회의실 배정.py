# https://www.acmicpc.net/problem/1931

N = int(input())
li = []
for i in range(N):
    a, b = map(int, input().split())
    li.append([a,b])
li.sort(key=lambda x : (x[1], x[0]))
cnt = 0
ans = []
for j in li:
    if j[0] >= cnt:
        ans.append(j)
        cnt = j[1]
print(len(ans))