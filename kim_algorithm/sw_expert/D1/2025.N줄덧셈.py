N = int(input())

result = 0              #반복문을 통해 1부터 입력받은 수까지 값을 result에 누적
for i in range(1, N+1):
    result += i         #이전 result 값에서 그 다음 값을 더한 값을 할당.
    

print(result)