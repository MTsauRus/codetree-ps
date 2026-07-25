V, E = map(int, input().split())
G = [[100001]*(V+1) for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    G[s][e] = min(G[s][e], w)

for i in range(1, V+1):
    G[i][i] = 0

for t in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if G[i][j] > G[i][t] + G[t][j]:
                G[i][j] = G[i][t] + G[t][j]

for j in range(1, V+1):
    for i in range(1, V+1):
        print(G[j][i], end=" ") if G[j][i] != 100001 else print(-1, end=" ")
    print()