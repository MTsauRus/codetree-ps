N = int(input())
str = input()
ans = 0
for i in range(N):
    for j in range(i+1, N+1):
        keyString = str[i:j]
        keyLen = j-i
        tmpSum = 0
        for k in range(N-keyLen+1):
            if keyString == str[k:k+keyLen]:
                tmpSum += 1
        if tmpSum >= 2:
            ans = max(ans, keyLen)

print(ans+1)