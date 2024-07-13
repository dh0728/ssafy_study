A, B = map(int, input().split())
result = "C"
if (A == 1 and B == 3) or (A ==2 and B == 1) or (A==3 and  B==2):
    result="A"
else:
    result="B"
print(result)
