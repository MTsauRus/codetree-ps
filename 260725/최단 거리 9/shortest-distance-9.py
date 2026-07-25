from heapq import heappush, heappop
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, d = map(int, input().split())
    G[s].append((d, e))
    G[e].append((d, s))

start, end = map(int, input().split())
dist = [float('inf') for _ in range(V+1)]
prev = [float('inf') for _ in range(V+1)]
dist[start] = 0

def dijkstra(start):
    pq = [(0, start)]

    while pq:
        cw, cv = heappop(pq)
        if cw > dist[cv]: continue # 낡은 경로 버리기
        
        for nw, nv in G[cv]:
            dist_next = cw + nw
            if dist[nv] > dist_next:
                dist[nv] = dist_next
                prev[nv] = cv # 어디에서 왔는지 기록
                heappush(pq, (dist_next, nv))

dijkstra(start)

print(dist[end])
ans = [end]
now = end

while now != start:
    
    ans.append(prev[now])
    now = prev[now]
print(*ans[::-1])