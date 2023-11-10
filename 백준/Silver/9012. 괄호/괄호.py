import sys

input = sys.stdin.readline

T = int(input())    # 반복 수


for _ in range(T):
    stk = []
    isVPS = True
    inputV = input().rstrip()   # 개행제거
    #inputV = input()


    for i in inputV:
        if i == '(':    # 왼쪽 괄호일경우 스택에 넣어주고
            stk.append(i)
        else:
            if len(stk) > 0:    # 스택에 값이 있다면 (팁, len(stk) > 0 == stk 같다.)
                stk.pop()   # 오른쪽 괄호라면 스택에서 빼준다.
            else:
                isVPS = False
                break


    if stk:
        isVPS = False # 스택에 값이 남아있다면 ex) (( 안닫힌 왼쪽괄호 false

    print('YES' if isVPS else 'NO') # 삼항연산자 isVPS가 true이면 YES 아니면 NO


    # if isVPS == True:
    #     print("YES")
    # else :
    #     print("NO")





