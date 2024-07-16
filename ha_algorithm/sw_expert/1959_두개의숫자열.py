#수정중..

def max_mul(N, M, Ai, Bj):
    if N > M:
        N, M = M, N
        Ai, Bj = Bj, Ai
    
    max_sum = 0
    
    for start in range(M - N + 1):
        current_sum = 0
        for i in range(N):
            current_sum += Ai[i] * Bj[start + i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    
    result = max_mul(N, M, Ai, Bj)
    print('#%d %d' % (t, result))
    #print(f'#{t} {result}')