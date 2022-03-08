N = list(input())
N.sort(reverse=True)


answer = 0
if "0" not in N:
    print(-1)
else:
    for i in N:
        answer += int(i)
    if answer % 3 != 0:
        print(-1)
    else:
        print("".join(N))

### clean code

import sys

n = list(sys.stdin.readline().rstrip())
n.sort(reverse=True)
if n[-1] != '0' or sum(map(int, n)) % 3 != 0:
    print(-1)
else:
    print(''.join(n))