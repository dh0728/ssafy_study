T = int(input())

month_31 = [1, 3, 5, 7, 8, 10, 12]
month_30 = [4, 6, 9, 11]

for test_case in range(1, T + 1):
    a=input()
    YYYY = a[:4]
    MM = a[4:6]
    DD = a[6:8]
    

    if 1 <= int(MM) <= 12:
        if int(MM) == 2 and 1 <= int(DD) <= 28:
            print(f'#{test_case} {YYYY}/{MM}/{DD}')
        elif int(MM) in month_31  and 1 <= int(DD) <= 31:
            print(f'#{test_case} {YYYY}/{MM}/{DD}')
        elif int(MM) in month_30 and 1 <= int(DD) <= 30:
            print(f'#{test_case} {YYYY}/{MM}/{DD}')
        else:
            print(f'#{test_case} -1')
    else:
        print(f'#{test_case} -1')