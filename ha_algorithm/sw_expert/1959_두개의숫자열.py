#수정중..

def max_mul(N, M, Ai, Bj):            #첫 번째 숫자열 길이, 두 번째 숫자열 길이, 첫 번쨰 숫자열, 두 번째 숫자열
    if N > M:                         #첫 번째 숫자열의 길이가 항상 짧도록 만들기
        N, M = M, N
        Ai, Bj = Bj, Ai
    
    max_sum = 0                       #변수 초기화
    
    for start in range(M - N + 1):    #위치 옮겨가기
        current_sum = 0
        for i in range(N):
            current_sum += Ai[i] * Bj[start + i]    #대응 요소 곱셈
        max_sum = max(max_sum, current_sum)    #current_sum이 max_sum보다 크면 max_sum을 current_sum으로 갱신
    
    return max_sum                    #최종 max_sum 반환

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())  #첫 번째 줄 N,M 정수 변환
    Ai = list(map(int, input().split()))    #두 번째 줄 Ai
    Bj = list(map(int, input().split()))    #세 번쨰 줄 Bj
    
    result = max_mul(N, M, Ai, Bj) # 함수 호출해서 최댓값 계산
    print('#%d %d' % (t, result))
    #print(f'#{t} {result}')
