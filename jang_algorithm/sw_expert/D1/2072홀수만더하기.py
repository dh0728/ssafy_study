T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input().split()))
    A = []
    for a in N:
        if a % 2 != 0:
            A.append(a)
    print(f'#{tc} {sum(A)}')