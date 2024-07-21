T = int(input())

for test_case in range(1, T + 1):
    a=list(map(int, input().split()))

    if a[0] < a[1]:
        print(f"#{test_case} <")
    elif a[0] == a[1]:
        print(f"#{test_case} =")
    else:
        print(f"#{test_case} >")

        