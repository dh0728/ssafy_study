def bus_route(N, bus_stop, P, C):
    blank_bus = [0] * P
    for i in range(P):
        count = 0
        for bus in bus_stop:
            if bus[0] <= C[i] <= bus[1]:
                count += 1
        blank_bus[i] = count

    answer = ' '.join(map(str, blank_bus))

    print(f'#{test_case} {answer}')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    bus_stop = [list(map(int,input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]

    bus_route(N, bus_stop, P, C)