import sys
input = sys.stdin.readline
from heapq import heappush, heappop

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
global_dist = [[10**9]*(V+1) for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    G[s].append((w, e))
    G[e].append((w, s))
    global_dist[s][e] = w
    global_dist[e][s] = w

start, end = map(int, input().split())
dist = [float('inf')] * (V+1)
# 뒤에서 시작하는 다익스트라
dist[end] = 0
# 기본 다익스트라
def dijkstra(start):
    pq = [(0, start)]

    while pq:
        cw, cv = heappop(pq)
        if cw > dist[cv]: continue

        for nw, nv in G[cv]:
            next_dist = cw + nw
            if dist[nv] > next_dist:
                dist[nv] = next_dist

                heappush(pq, (next_dist, nv))

dijkstra(end)
print(dist[start])
now = start
path = [start]
while now != end:
    mv = 100001 # min_vertex
    for nw, nv in G[now]:
        if dist[now] == dist[nv] + nw: # now -> nv로 가는 weight == nw
            if nv < mv:
                mv = nv
    
    path.append(mv)
    now = mv
    mv = 100001
        

print(*path)
