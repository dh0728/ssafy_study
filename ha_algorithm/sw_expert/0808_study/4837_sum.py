T = int(input()) # 3 가정
for test_case in range(1, T + 1):
    N,K = map(int,input().split()) # N=3 / K=6 가정
 
    result_count = 0
    A_set_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(A_set_list)
    subsets = []
    subset_count = 2**n # 2의3승 -> 8
 
    for i in range(subset_count): # 0~7, 총 8번 순회
        subset = []
        for j in range(n): # 0~2, 총 3번(부분집합의 원소 수) 순회
            if i & (1 << j):
                subset.append(A_set_list[j])
        subsets.append(subset)
 
    for subset in subsets:
        if len(subset) == N and sum(subset) == K:
            result_count += 1
        else:
            result_count += 0
 
    print(f'#{test_case} {result_count}')