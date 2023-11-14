# 시작 위치와 도착 위치도 포함한다.
import sys
from collections import deque
# sys.stdin = open("./input", "r")
input = sys.stdin.readline
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
N, M = map(int, input().split())
board = [input() for _ in range(N)] # 붙어서 주어져서 string으로 받음

# 아래는 보드 체크 확인용
# for i in board:
#     print(i)

def is_vaild(y, x):
    return 0 <= y < N and 0 <= x < M


def bfs():
    chk = [[False]*M for _ in range(N)]
    chk[0][0] = True    # 시작점
    dq = deque()
    dq.append((0, 0, 1))    # y, x, 몇 칸을 밟았는지 1인 이유는 시작칸도 센다고 명시되어있어서
    while dq:
        y, x, d = dq.popleft()
        nd = d + 1

        if y == N-1 and x == M-1:   # 가장 우하단으로 내려온경우 index값이 0부터 시작이라 -1해준다.
            return d    # 몇 칸

        for k in range(4):  # 네 방향
            ny = y + dy[k]
            nx = x + dx[k]
            # 0보다 크고 N보다 작으며(1줄안에 들어오는 범위) and 1인 구간만 지나갈 수 있고 and 처음가는 길인 경우
            if is_vaild(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True  # 방문체크
                dq.append((ny, nx, nd)) # dq에 넣어준다.
    # return -1 # 항상 도착지점에 도착하는게 아니라 못 도달하는 경우 -1을 출력해라 하는 경우에 써준다.

print(bfs())
