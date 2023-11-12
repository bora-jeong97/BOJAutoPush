import sys

y, x = map(int, sys.stdin.readline().split())

lst1 = []
lst2 = []
tmp = []

# 첫 행렬 입력
for i in range(0, y):
    tmp =list(map(int, sys.stdin.readline().split()))
    lst1.append(tmp)
    tmp = []
#print(lst1)
# 두번째 행렬 입력
for i in range(0, y):
    tmp =list(map(int, sys.stdin.readline().split()))
    lst2.append(tmp)
    tmp = []
#print(lst2)

# 출력
for i in range(0, y):
    for j in range(0, x):

        print(f"{lst1[i][j] + lst2[i][j]}", end=" ")
    print("")