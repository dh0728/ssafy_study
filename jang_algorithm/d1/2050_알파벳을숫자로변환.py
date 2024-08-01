N = input()
A = []
for a in N:
    A.append(int(ord(a)) - 64)
    
print(*A)
