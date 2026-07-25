N, M = map(int, input().split())
arr = list(map(int, input().split()))

def find(key):
    lo = 0
    hi = N-1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] < key:
            lo = mid+1
        
        # hi는 같을때에도 내려야 함
        else:
            hi = mid-1

    if 0 <= lo < N and arr[lo] == key:
        return lo+1
    
    else:
        return -1

query = list(map(int, input().split()))
for i in range(M):
    print(find(query[i]))