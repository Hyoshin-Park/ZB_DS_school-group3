# url = "https://euleroj.io/problemset/viewer/2007"
# # 상단 부분, 허리 부분, 하단부분으로 나눠서 출력함
n=5
# 상단 부분
for i in range(1, n):
    for j in range(1, i+1):
        print(j, end = "") # 좌측날개
    print(" " * ((n-1) * 2 - (i * 2 -1)), end = "") # 공백
    for j in range(i, 0, -1):
        print(j, end="") # 우측날개
    print()
# 허리부분
for i in range(1, n+1):
    print(i % 10, end = "") #1부터 5까지 나타나며, 10이 넘어갈경우, 0을출력해야 함
for i in range(n-1 , 0, -1):
    print(i, end = "") # 1부터 4까지
print()
# 하단부분
for i in range(n-1,0,-1):
    for j in range(1, i+1):
        print(j, end= "")
    print(" " * ((n-1) * 2 - (i * 2 -1)), end="")
    for j in range(i, 0, -1):
        print(j,end="")
    print()
