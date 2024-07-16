N= int(input())
four=N%4
hun=N%100
both=N%400

if (four ==0 and hun != 0) or both == 0:
    print(1)
else:
    print(0)
