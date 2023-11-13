import sys


N = int(input()) # 오늘 팔린 책의 개수
lst = []

# 입력
for i in range(0, N):
    lst.append(input())

lst.sort()   # 오름차순 사전 순으로 가장 앞서는 제목을 출력


max=0
result =""

for i, v in enumerate(lst):
    # print("i는? : ", i)  # 인덱스 반환
    # print("v는? : ", v)  # 값을 반환
    # print("i의 수는 ? ", lst.count(v))
    if(max < lst.count(v)):
        max = lst.count(v)
        result = v

print(result)


