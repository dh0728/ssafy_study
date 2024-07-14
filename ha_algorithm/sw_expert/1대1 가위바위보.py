A, B = map(int, input().split())
 
if A + B == 4 :
    print('A' if A == 1 else 'B')
else:
    print('A' if A > B else 'B')