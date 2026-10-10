import sys
input = sys.stdin.readline

N, M = map(int, input().split())
boxes = {}
G = [[0]*(N+1) for _ in range(N+1)]

def check_left(k):
    nh, nw, nc, nr = boxes[k]
    col = nc - 1

    flag = False

    while col > 0 and flag is False:
        for r in range(nr - nh + 1, nr + 1):
            if G[r][col] != 0:
                flag = True
                break
        col -= 1

    return not flag

def check_right(k):
    nh, nw, nc, nr = boxes[k]
    for col in range(nc+nw, N+1):
        for r in range(nr-nh+1, nr+1):
            if G[r][col]:
                return False
    return True

def delete(k):
    nh, nw, nc, nr = boxes[k]
    for r in range(nr-nh+1, nr+1):
        for c in range(nc, nc+nw):
            G[r][c] = 0
    del boxes[k]
    for j in sorted(boxes, key=lambda x: -boxes[x][3]):
        down(j)

def down(k):
    # boxes 업데이트
    global G
    nh, nw, nc, nr = boxes[k]

    # 원래자리 0 처리 (연쇄 재활용)
    for r in range(nr-nh+1, nr+1):
        for c in range(nc, nc+nw):
            G[r][c] = 0

    # 바닥이거나 더 못내려갈때까지
    row = nr
    flag = False
    while row < N and flag == False:
        for c in range(nc, nc+nw):
            if G[row+1][c] != 0:
                flag = True
                row -= 1
                break

        row += 1

    # 탈출했으면 바닥 or 걸린거니까 boxes 업데이트하고 G 표시
    boxes[k] = (nh, nw, nc, row)
    for r in range(row-nh+1, row+1):
        for c in range(nc, nc+nw):
            G[r][c] = k


for _ in range(M):
    k, h, w, c = map(int, input().split())
    boxes[k] = (h, w, c, h) # [4]: row, 하단 기준
    down(k)

left = True

for _ in range(M):
    for box in sorted(boxes):
        if left:
            if check_left(box):
                # delete함수: G에서 제거해주고 그 위에놈들 싹 순회해서 down처리
                print(box)
                delete(box)
                left = False
                break
        else:
            if check_right(box):
                print(box)
                delete(box)
                left = True
                break


