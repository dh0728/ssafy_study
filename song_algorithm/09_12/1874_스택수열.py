def cnt_operator():
    stack = []
    max_n = 0
    for _ in range(N):
        n = int(input())
        if not stack:  # 비어있으면 그냥 push
            for i in range(max_n + 1, n + 1): # max_n+1 에서 n까지 차례대로 스택에 삽입
                stack.append(i)
                result.append('+') # push된만큼 + 삽입
            stack.pop() # 입력된 정수 pop으로 빼기
            result.append('-')
            if max_n < n: # 현재까지 stack에 들어간 정수값으로 max_n 교체
                max_n = n
        else:
            if n < max_n: # 현재까지 스택에 들어간 정수값보다 작다면 pop
                if stack.pop() != n: # n과 pop한게 다르면 불가능한 경우
                    return 0
                result.append('-')
            else: # 현재까지 스택에 들어간 정수값보다 크다면
                for i in range(max_n + 1, n + 1): # max_n+1 에서 n까지 차례대로 스택에 삽입
                    stack.append(i)
                    result.append('+')
                if stack.pop() != n: # n과 pop한게 다르면 불가능한 경우
                    return 0
                result.append('-')
                max_n = n
    return 1 # 함수가 끝까지 작동하면 가능한 경우= 1 리턴

N=int(input())
result=[]
res=cnt_operator()
if res:
    for r in result:
        print(r)
else:
    print('NO')
