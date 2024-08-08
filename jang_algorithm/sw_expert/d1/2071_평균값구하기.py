T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input().split()))
    A = []
    sums = 0
    for n in N:
        sums += n
        A.append(sums)
    result = A[-1] / len(N)
    print(f'#{tc} {int(round(result, 0))}')
