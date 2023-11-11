from collections import deque
import sys

inp = sys.stdin.readline
N = int(inp().rstrip())

#print("출력 :  ", N)

#  dq에 값 넣기
dq = deque()
for i in range(1, N+1):  # 1부터 N까지 range는 1, 2, 3, ... n-1
    dq.append(i)
#print("입력된 dq : ", dq)

# 연산
while len(dq) > 1:  # 1이 남을 때까지 반복
 #   print("현재 dq : ", dq)
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])
#print("마지막 남은dq : ", dq[0])
