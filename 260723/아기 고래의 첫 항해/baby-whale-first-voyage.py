from collections import deque

N, sr, sc, sd = map(int, input().split())
sr = sr - 1
sc = sc - 1
sd = sd - 1
G = []
for _ in range(N):
    G.append(list(map(int, input().split())))

visited = [[False for _ in range(N)] for _ in range(N)]
# 시작좌표 넣고시작
#ans = [(sr, sc, sd)]
visited[sr][sc] = True

iter = 0
# 루프 횟수 세기
for i in range(N):
    for j in range(N):
        if G[i][j] == 0: iter+=1

r = sr
c = sc
d = sd

# 1번이동방식: 상하좌우
dr1 = [-1, 1, 0, 0]
dc1 = [0, 0, -1, 1]
# 2번이동방식: 좌하우상
dr2 = [0, 1, 0, -1]
dc2 = [-1, 0, 1, 0]

def move1():
    global r, c, d, visited, ans
    # 이동가능하다면 ans에 추가하고 나와

    # 여기에서만 쓸 drr, dcc 정의
    if d == 0:
        drr = [-1, 0, 0, 1]
        dcc = [0, -1, 1, 0]
    elif d == 1:
        drr = [1, 0, 0, -1]
        dcc = [0, 1, -1, 0]
    elif d == 2:
        drr = [0, 1, -1, 0]
        dcc = [-1, 0, 0, 1]
    else:
        drr = [0, -1, 1, 0]
        dcc = [1, 0, 0, -1]

    for i in range(4):
        nr = r + drr[i]
        nc = c + dcc[i]

        # 이동가능하다면 r, c 업뎃, visited처리
        if 0 <= nr < N and 0 <= nc < N and G[nr][nc] == 0 and not visited[nr][nc]:
            visited[nr][nc] = True
            r = nr
            c = nc
            # 다음 방향 정의
            if drr[i] == -1:
                d = 0
            elif drr[i] == 1:
                d = 1
            elif dcc[i] == -1:
                d = 2
            else:
                d = 3
            #ans.append((nr, nc, d)) # 다음좌표추가
            return True
        
    # 이동 불가
    return False
    

def find():
    # bfs 전체 한번 돌리자. 
    # 그렇게 돌린 dist G를 구하고, 최솟값 후보를 뽑자. row -> col 순으로 순회하면 되고, 동점인 경우까지 스킵
    # 가장 작은 케이스만 return을 업데이트하면 됨!
    # 참고로 순회할 때 visited가 false여야 함 암초도 아니어야하고 까먹지마시길
    dq = deque([(r, c)])
    dist = [[100001] * N for _ in range(N)]
    dist[r][c] = 1
    while dq:
        nowr, nowc = dq.popleft()
        for i in range(4):
            nr = nowr + dr1[i]
            nc = nowc + dc1[i]
            # 방문안했고 암초아니면
            if 0 <= nr < N and 0 <= nc < N and dist[nr][nc] == 100001 and G[nr][nc] == 0:
                # 방문처리했고
                dist[nr][nc] = dist[nowr][nowc] + 1
                # 덱에넣고
                dq.append((nr, nc))

    er = -1
    ec = -1
    min_dist = 100000
    # 다음 행선지 찾기
    for i in range(N):
        for j in range(N):
            # 암초도 아니어야하고 글로벌 visited도 아니어야 함
            if dist[i][j] < min_dist and G[i][j] == 0 and not visited[i][j]:
                er = i
                ec = j
                min_dist = dist[i][j]
    # 리턴 er ec
    #print("다음은 ", er+1, ec+1)
    return er, ec

def move2(er, ec):
    global r, c, d, visited, ans
    # ans에 추가하고 나와
    visited_move2 = [[False for _ in range(N)] for _ in range(N)]
    visited_move2[r][c] = True
    # 좌하우상으로 bfs, 이전칸을 통해 방향까지 같이 저장
    dq = deque([(r, c, d)])
    while dq:
        nowr, nowc, nowd = dq.popleft()
        for i in range(4):
            nr = nowr + dr2[i]
            nc = nowc + dc2[i]
            if 0 <= nr < N and 0 <= nc < N and not visited_move2[nr][nc] and G[nr][nc] == 0:
                # 방향먼저 구하고
                # 다음 방향 정의
                if dr2[i] == -1:
                    d = 0
                elif dr2[i] == 1:
                    d = 1
                elif dc2[i] == -1:
                    d = 2
                else:
                    d = 3
                # er ec 체크해서 트루면 리턴
                if nr == er and nc == ec:
                    r = er
                    c = ec
                    #print("move2 이동완료", r+1, c+1)
                    return
                visited_move2[nr][nc] = True
                dq.append((nr, nc, d))
                

print(sr+1, sc+1)
for i in range(iter-1): # 시작좌표 빼고 시작
    if move1():
        print(r+1, c+1)

    else: 
        #(안되면) 2번이동시도
        # 먼저 최단거리 도달점 찾기
        # 찾은 도달점으로 좌하우상 순으로 이동하기
        er, ec = find()
        move2(er, ec)
        # 다음 행선지도 True 처리
        visited[er][ec] = True
        print(er+1, ec+1)