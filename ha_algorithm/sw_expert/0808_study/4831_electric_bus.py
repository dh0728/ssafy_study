T = int(input())
for test_case in range(1,T+1):
    K, N, M = map(int, input().split())
    bus_number = list(map(int, input().split())) + [N]
    i = 0
    count = 0
    while i+K < N:
        for j in range(len(bus_number)-1):
            if i+K == bus_number[j]:
                i = bus_number[j]
                count += 1
            elif i+K > bus_number[j] and i+K < bus_number[j+1]:
                i = bus_number[j]
                count += 1
            elif i+K < bus_number[j]:
                if i+K < bus_number[j+1]:
                    print('0')
                    break
                if i+K >= bus_number[j+1]:
                    i = bus_number[j]


    print(count)
