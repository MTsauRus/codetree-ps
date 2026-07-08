K, N = map(int, input().split())

def sol(arr, idx, depth):
    if depth == N:
        print(*arr)
        return

    for i in range(idx, K+1):
        sol(arr + [i], idx, depth + 1)

sol([], 1, 0)