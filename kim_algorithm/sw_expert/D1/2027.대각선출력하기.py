for i in range(5):
    for j in range(5):
        if i == j:
            print('#', end='')
        else:
            print('+', end='')
    print()


# 비트 연산 시프트 사용 
for i in range(5):                  #0b10000 를 슬라이싱 하고 0b 날려줌
    st=bin(16>>i)[2:].zfill(5)      #zfill 문빈칸을 0으로 채우는
    for s in st:
        if s=='1':print("*",end='')
        else:print("+",end='')
    print()


