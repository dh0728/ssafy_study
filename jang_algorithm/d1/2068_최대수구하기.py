T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input().split()))
    A = []
    for n in N:
        A.append(max(N))
    result = A[-1]
    print(f'#{tc} {result}')