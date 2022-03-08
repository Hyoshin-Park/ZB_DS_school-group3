#https://www.acmicpc.net/problem/9012

# N = int(input())
# for _ in range(N):
#     word = input()
#     cnt = 0
#     for i in word:
#         if cnt == -1:
#             break
#         else:
#             if i == '(':
#                 cnt += 1
#             else:
#                 cnt -= 1
#     if cnt == 0:
#         print("YES")
#     else:
#         print("NO")

for _ in range(int(input())):
    s=input()
    for z in s:
        s=s.replace('()','')
        print(s)
    print(s and 'NO' or 'YES')


# print(1 and 0 or 2 and 3)
# print(1 and 2 or 0 and 3)
# print(0 and 2 or 0 and 3)
# print(0 or 1 or 0 and 2)
