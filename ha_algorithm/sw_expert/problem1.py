'''
i번째 버튼을 누르면 i의 배수...에 해당하는 등의 상태 바뀜
모두 꺼진 상태에서... 원하는 패턴을 만들기 위한 최소 스위치 조작 횟수
출력 -> 최소 스위치 조작 횟수
'''
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    pattern = [0] + list(map(int, input().split()))
    first_list = [0] * (N+1)
    cnt = 0

    while pattern != first_list:
        for i in range(1, N + 1):
            if pattern[i] == first_list[i]: continue
            if first_list[i] == 0:
                cnt += 1
                for j in range(1, (len(pattern)-1)//i + 1):
                    if first_list[i*j] == 0:first_list[i*j] = 1
                    else: first_list[i*j] = 0
            elif first_list[i] == 1:
                cnt += 1
                for j in range(1, (len(pattern)-1)//i + 1):
                    if first_list[i * j] == 0:
                        first_list[i * j] = 1
                    else:
                        first_list[i * j] = 0

    print(f'#{test_case} {cnt}')

























    # for but, stat in enumerate(pattern):
    #     if stat == 1: on_list.append(but)
    # for i in range(1, len(on_list)):
    #     if on_list[i] == 1:
    #         cnt += 1
    #         first_list[1] = 1
    #         continue
    #     for j in range(i+1, len(on_list)):
    #         if on_list[j] % on_list[i] == 0: on_list.pop(j)
    #
    # while first_list != pattern:
    #     for a in on_list:
    #         if a == 0: continue
    #         cnt += 1
    #         for k in range(1, (len(pattern)-1)//a +1):
    #             if first_list[j*k] == 0: first_list[j*k] = 1
    #             else: first_list[j*k] = 0
    #
    # print(cnt)



