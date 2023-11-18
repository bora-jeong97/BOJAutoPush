

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    board = []
    max = 0

    # 보드 생성
    board = [list(map(int, input().split())) for _ in range(n)]


    # 시작점
    for y in range(n-m+1):
        for x in range(n-m+1):

            # 시작점부터 파리채 범위까지의 합
            tmp = 0
            for ny in range(y, y+m):
                for nx in range(x, x+m):
                    tmp += board[ny][nx]

            if max < tmp:
                max = tmp


    print(f"#{test_case} {max}")