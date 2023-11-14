import sys
# sys.stdin = open("./input", "r")
# time python part2/chapter4_graph/11724.py < ./input

# 아래는 재귀함수 depth가 1000이 최대인데 그걸 늘려주는 함수이다.
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())    # 노드와 간선의 수
adj = [[0]* N for _ in range(N)]    # 노드의 수의 제곱만큼 0으로 초기화

# 인접행렬 생성
for _ in range(M): # 간선만큼 값을 받아준다.
    # N값이 1부터 시작하기 때문에 인덱스 값을 받기 위해 -1을 해준다.
    a, b = map(lambda x: x-1, map(int, input().split()))
    adj[a][b] = adj[b][a] = 1   # 양방향 그래프는 대칭이기 때문

# 인접행렬 확인용
# for row in adj:
#     print(row)

ans = 0 # 연결요소 개수
chk = [False] * N   # 체크는 False로 초기화

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:   # 인접행렬에 1로 존재 + 한번 방문한 노드는 재 방문 안함
            chk[nxt] = True
            dfs(nxt)



for i in range(N):  # 노드만큼 체크
    if not chk[i]:  # False라면? 체크 안된 곳이라면?
        ans += 1
        chk[i] = True # 체크해준다.
        dfs(i)


print(ans)
# 제출 전에 테스트 케이스를 직접 만들어 보는것이 좋다.
# 최소, 최대를 넣어보는 것이 좋다.