import heapq as hq
import sys
# 우선순위큐
input = sys.stdin.readline

# 입력
arr = []
for _ in range(int(input())):   # 해당 값의 횟수만큼 반복
    x = int(input())

    if x : # x가 0이 아니면
        hq.heappush(arr, (abs(x), x))    # 튜플에 절대값과, 해당값을 같이 저장해준다.
    else:  # x값으로 0이 들어오면
        # 튜플 전체가 다 나오지 않도록 [1] x값을 얻게 해둔다.
        print(hq.heappop(arr)[1] if arr else 0)    # 삼항연산자로 아래글 갈음가능
       # if arr: # 값이 남아있으면
       #     print(hq.heappop(arr)[1])   # 가장 작은값을 삭제하고 출력한다
       # else :   # 값이 없으면
       #     print(0) # 0반환
