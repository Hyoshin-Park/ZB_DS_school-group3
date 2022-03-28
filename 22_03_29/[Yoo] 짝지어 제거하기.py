def solution(s):
    s = list(s)
    n = 0
    s.append('!')
    while True:
        if n >= len(s)-2:
            break
        if s[n] == s[n+1]:
            s.pop(n)
            s.pop(n)
            n = 0
            continue
        else:
            n += 1
    s.pop()
    if len(s) == 0:
        return 1
    else:
        return 0

print(solution('baabaa'))         