A,B=map(int, input().split())
a=A-B
if a>0:
    print('>')
elif a<0:
    print('<')
else:
    print('==')
