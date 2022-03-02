# a, b = input().split()
# answer = []

# max_a = ''
# max_b = ''
# min_a = ''
# min_b = ''
# #최솟값
# for i in a:
#     if i == '6':
#         min_a += '5'
#     else:
#         min_a += i

# for j in b:
#     if j == '6':
#         min_b += '5'
#     else:
#         min_b += j
# #최댓값
# for k in a:
#     if k == '5':
#         max_a += '6'
#     else:
#         max_a += k

# for l in b:
#     if l == '5':
#         max_b += '6'
#     else:
#         max_b += l

# answer.append(int(min_a) + int(min_b))
# answer.append(int(max_a) + int(max_b))
# result = ''
# for n in answer:
#     result += str(n) + " "
# print(result.strip())



##깔끔한 코드
a, b = input().split()
min = int(a.replace('6', '5')) + int(b.replace('6', '5'))
max = int(a.replace('5', '6')) + int(b.replace('5', '6'))
print(min, max)
