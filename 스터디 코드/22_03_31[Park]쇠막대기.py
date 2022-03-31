https://www.acmicpc.net/problem/10799

word = list(input())

cnt = 0
stack = []

for i in range(len(word)):
    if word[i] == "(":
        stack.append("(")
    else:
        if word[i-1] == "(":
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt)
