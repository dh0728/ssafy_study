li = list(map(int, input()))
print(sum(li))


# 버전2 리스트로 만들어서 더하기
print(sum(list(map(int, input()))))

# 버전3 반복문 사용해서 더하기
print(sum(int(a) for a in input()))

# 버전4 그냥
print(sum(map(int,input())))