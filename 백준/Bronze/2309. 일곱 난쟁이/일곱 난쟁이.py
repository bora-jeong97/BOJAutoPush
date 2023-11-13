'''
9명중에 7명을 뽑아라
오름차순으로 출력한다.
순서상관없음 - > 조합
'''
from itertools import combinations
# 9명 입력
lst = []
for i in range(9):
    lst.append(int(input()))

result= []
# 9명중에 7명 조합
for i in combinations(lst, 7):
    #print("i : ",i)
    #print(i[0])
    sum = 0
    for j in range(7):
        type(i[j])
        sum += int(i[j])
    if(sum == 100):
        result.append(i)


# 오름차순 출력
re = list(result[0])
re.sort()
for i in re:
    print(i)
#   시간 측정
#   time python part2/chapter2_bruteForce/2309.py < ./input





