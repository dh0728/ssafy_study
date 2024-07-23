T = int(input())

for test_case in range(1, T+1):
    li = list(map(int, input().split()))
    li.sort()
    print(f'#{test_case} {li[-1]}')

    #방법2
    n = max(list(map(int, input().split())))
    print(f'#{test_case} {n}')
