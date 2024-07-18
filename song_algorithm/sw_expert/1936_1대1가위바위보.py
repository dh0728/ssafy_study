# A, B = map(int, input().split())
# result = "C"
# if (A == 1 and B == 3) or (A ==2 and B == 1) or (A==3 and  B==2): # A가 이기는 경우
#     result="A"
# else:
#     result="B"
# print(result)

# #버전2 
# A,B=map(int,input().split())
# a=A-B
# if a==-1 or  a==2 : 
#     print('B')
# else:
#     print('A')

# A,B=map(int,input().split())
# if (A-B)%3==1:
#     print('A')
# else:
#     print('B')

#버전4
A,B=map(int,input().split())
print('AB'[(A-B)%3==2])

print(-4//3)