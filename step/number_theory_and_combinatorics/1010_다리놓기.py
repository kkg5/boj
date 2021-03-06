import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k, n = map(int, input().split())
    ans = 1

    for i in range(n, n-k, -1):
        ans *= i

    for i in range(1, k+1):
        ans //= i

    print(ans)