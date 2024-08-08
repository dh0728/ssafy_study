import sys
sys.stdin = open("부분집합_input.txt")

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(A)
    subset_cnt = 2**n

    subsets = []
    for i in range(subset_cnt):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(A[j])
            subsets.append(subset)

    # print(subsets)



'''
A 안의 리스트들 중 길이가 N인 부분집합들만 꺼내기
    subsets_A = []
    for a in range(A):
        if len(a) == N:
            subset_A.append(a)
subset_A 순회하면서 요소 더했을 때 K인 리스트들 개수 출력  
    sums = []
    for b in range(subset_A):
        if sum(b) == K:
            sums.append(b)
    result = len(sums)

    print(f'#{test_case} {result}')
    
'''