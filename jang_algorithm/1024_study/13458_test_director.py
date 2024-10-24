n = int(input())  # 시험장 수
people = list(map(int, input().split()))  # 시험장 별 응시자 수
a, b = map(int, input().split())  # 감독관이 감독할 수 있는 응시자 수

cnt = n  # 총감독관한명씩은 무조건 포함이라 n 할당
for i in people:
    i -= a  # 우선 총감독관 학생수 빼주고
    if i > 0:  # 남은 수가 0보다 크면
        if i % b != 0:  # 남은 응시자수와 부감독 나눴을때 0이 아니면 몫 +1
            cnt += (i//b)+1
        else:  # 0이면 몫만 더하기
            cnt += (i//b)
print(cnt)
