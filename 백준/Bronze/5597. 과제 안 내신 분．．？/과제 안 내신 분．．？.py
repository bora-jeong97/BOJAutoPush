from sys import stdin

lst = [*range(1, 31)]   # 1부터 31까지 넣어라
#stdin.readline()
for i in range(0, 28):
    stu = int(stdin.readline())
    lst.remove(stu)

print(lst[0])
print(lst[1])