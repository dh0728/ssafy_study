#수정중..
for t in range(int(input())): #test case 수 입력 받은 만큼 반복
    N = int(input()) #각 테스트 케이스마다 행렬 크기(줄) N 입력받기
    input_li = [input().split() for i in range(N)] #list comprehension 사용 N번 반복 후 input_li 리스트에 저장
    result = [""] * N #회전 후 결과 저장 리스트 빈 문자열로 초기화
     
    # CASE 1
    res_li_1 = [[]] * N #N개의 빈 리스트 초기화
    for li in input_li : #각 행을 순회해서 반복
        for i, v in enumerate(li) : #각 행의 인덱스와 값 반복 #enumerate는 리스트 순회하면서 인덱스랑 값을 동시에 가져옴
            res_li_1[i] = res_li_1[i] + [v] #회전된 값 추가
 
    for i, li in enumerate(res_li_1) : 
            result[i] += "".join(li) 
 
    # CASE 2
    for i, li in enumerate(input_li) :
            result[N - i - 1] += f" {''.join(list(reversed(li)))}" #역순으로 저장하려고 #앞에 공백주기
 
    # CASE 3
    res_li_3 = [[]] * N
    for li in input_li : 
        for i, v in enumerate(li) :
            new_i = N - i - 1 #역순 저장
            res_li_3[new_i] = res_li_3[new_i] + [v]
 
    for i, li in enumerate(res_li_3) :
            result[i] += f' {"".join(li)}' #앞에 공백주기
 
    print(f"#{t+1}") # '#1' 부터 시작
    for s in result :
            print(s) # 한 줄씩 출력하기