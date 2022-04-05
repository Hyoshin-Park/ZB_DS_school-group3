OneNineList = [i for i in range(1, 10)]
Sudoku = []
for i in range(9):
    tmp = list(map(int, input().split()))
    Sudoku.append(tmp)

flag = True
for i in range(0, 9): # 가로
    tmp = Sudoku[i]
    if sorted(tmp) == OneNineList:
        pass
    else:
        flag = False
        pass
    
    tmpList = []    
    for j in range(0, 9): # 세로
        tmpList.append(Sudoku[j][i])

    if sorted(tmpList) == OneNineList:
        continue
    else:
        flag = False
        break
for k in range(0, 9, 3):
    for l in range(0, 9, 3):
        tmpList = []
        for i in range(l, l+3):
            for j in range(k, k+3):
                tmpList.append(Sudoku[j][i])
        if sorted(tmpList) == OneNineList:
            pass
        else:
            flag=False
if flag == True:
    print("YES")
else:
    print("NO")
