T = int(input())

for test_case in range(1, T + 1):
    # S = []
    b, c = map(int, input().split())
    result1 = b // c
    result2 = b % c
    # S.append(result1)
    # S.append(result2)
    

    print(f'#{test_case} {result1} {result2}')