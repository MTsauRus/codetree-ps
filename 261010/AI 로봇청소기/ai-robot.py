from collections import deque
from copy import deepcopy
"""
1. 이동방식: 오염되고 && 가장 가까운거 -> 상 좌 우 하
2. 청소방식: ㅗ 모양, 합이 가장 큰거, 없으면 우 하 좌 상 순서, 각 격자마다 20
3. 모든 격자에 + 5
4. 깨끗한거 상하좌우 합 // 10만큼 먼지 확산
5. 전체 공간 먼지량 출력 or 없으면 0 후 종료
"""
N, K, L = map(int, input().split())
G = []

# 이동용 drdc
mdr = [-1, 0, 0, 1]
mdr = [-1, 0, 0, 1]
mdc = [0, -1, 1, 0]

# 로봇들
robots = {}

for _ in range(N):
    G.append(list(map(int, input().split())))

for k in range(K):
    a, b = map(lambda x: int(x) - 1, input().split())
    robots[k] = (a, b)

# 다음 청소칸을 찾는 메서드
def select_next(r, c):
    global N, K, L, G, robots

    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[r][c] = True
    
    # 확산에 의해 자기자리에 먼지가 생긴경우
    if G[r][c] >= 1:
        return r, c
    
    dq = deque([(r, c)])
    robot_sets = set(robots.values())
    while dq:
        cand = []
        for _ in range(len(dq)):
            r, c = dq.popleft()
            for i in range(4):
                nr = r + mdr[i]
                nc = c + mdc[i]
                # 좌표 유효, 미방문, 청소기도 없음
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and not ((nr, nc) in robot_sets):
                    # 만약 먼지가 있다면 그 좌표 바로 리턴
                    if G[nr][nc] >= 1:
                        cand.append((nr, nc))
                        dq.append((nr, nc))
                        visited[nr][nc] = True

                    # 먼지는 없는데 갈 수 있다면 덱에 넣자
                    elif G[nr][nc] == 0:
                        dq.append((nr, nc))
                        visited[nr][nc] = True
        if cand:
            return min(cand)

    # 청소할 칸이 없으면 -1
    return -1, -1



def move(k):
    global G, robots
    r, c = robots[k][0], robots[k][1]
    nr, nc = select_next(r, c)
    # 청소할 칸 없다면 걍 거기 있으세요
    if nr == -1:
        return r, c

    # 로봇 좌표 업데이트해주고
    robots[k] = (nr, nc)
    # 업뎃된 좌표를 리턴해줍시다.
    return nr, nc


def clean(k):
    global G, robots
    r, c = robots[k][0], robots[k][1]

    max_clean = 0
    max_dir = 0
    # 덧셈에 포함 안되는 칸 순서대로
    rem_r = [0, -1, 0, 1]
    rem_c = [-1, 0, 1, 0]

    dr = [0, 0, 0, 1, -1]
    dc = [0, 1, -1, 0, 0]

    for i in range(4):
        tmp = 0
        # 5방향 더하기
        for j in range(5):
            nr = r + dr[j]
            nc = c + dc[j]
            if 0 <= nr < N and 0 <= nc < N and G[nr][nc] >= 1:
                tmp += min(20, G[nr][nc])

        # 해당방향 빼주기
        rr = r + rem_r[i]
        rc = c + rem_c[i]
        if 0 <= rr < N and 0 <= rc < N and G[rr][rc] >= 1:
            tmp -= min(20, G[rr][rc])

        # 최댓값 업데이트
        if max_clean < tmp:
            max_clean = tmp
            max_dir = i

    # 진짜 G에서 빼주기

    rr = r + rem_r[max_dir]
    rc = c + rem_c[max_dir]
    for j in range(5):
        nr = r + dr[j]
        nc = c + dc[j]

        # 생략해도 되는칸은 안빼줍니다
        if rr == nr and rc == nc:
            continue

        if 0 <= nr < N and 0 <= nc < N and G[nr][nc] >= 1:
            if G[nr][nc] <= 20:
                G[nr][nc] = 0
            else:
                G[nr][nc] -= 20

def dirty():
    global G
    for i in range(N):
        for j in range(N):
            if G[i][j] >= 1:
                G[i][j] += 5

def spread():
    global G
    tmp_G = [[0] * N for _ in range(N)]
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    for r in range(N):
        for c in range(N):
            if G[r][c] == 0:
                tmp = 0
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < N and 0 <= nc < N and G[nr][nc] >= 1:
                        tmp += G[nr][nc]

                tmp_G[r][c] = tmp // 10

    for i in range(N):
        for j in range(N):
            G[i][j] += tmp_G[i][j]


def result():
    global G
    tmp = 0
    for i in range(N):
        for j in range(N):
            if G[i][j] >= 1:
                tmp += G[i][j]

    return tmp

for _ in range(L):
    for k in range(K):
        # 이동
        move(k)

    for k in range(K):
        # 청소
        clean(k)

    # 먼지축적
    dirty()
    # 먼지확산
    spread()
    # 출력
    ans = result()

    if ans == 0:
        print(0)
        exit(0)
    else:
        print(ans)