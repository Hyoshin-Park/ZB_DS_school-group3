# https://www.acmicpc.net/problem/2839

N = int(input())
ans = []
n = 0
while 5*n <= N:
    a = 5*n
    if (N - a) % 3 == 0:
        ans.append(n+(N-a)//3)
    n += 1
if ans == []:
    ans.append(-1)
print(min(ans))