
# 총 10번 반복
for test_cast in range(1, 11):
    result = 0
    N = int(input())    # 덤프횟수
    lst = list(map(int, input().split()))  # 집들의 높이

    mx = 0
    mn = 0
    # 덤프 횟수 만큼 반복
    for i in range(N):
        mx = max(lst)
        mn = min(lst)
        maxIndex = lst.index(mx)
        minIndex = lst.index(mn)
        if mx - mn > 1:
            lst[maxIndex] -= 1
            lst[minIndex] += 1

    mx = max(lst)
    mn = min(lst)
    #print(f"#{test_cast} max : {mx} min : {mn} result : {mx-mn}")
    print(f"#{test_cast} {mx-mn}")