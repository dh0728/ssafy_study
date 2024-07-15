A=int(input())
B=input()

#버전1
a=A*int(B[2])
b=A*int(B[1])
c=A*int(B[0])

print(a)
print(b)
print(c)
print(a+b*10+c*100)


#버전2
ls=[]
for i in range(len(B)-1,-1,-1):
    ls.append(A*int(B[i]))

print(ls[0])
print(ls[1])
print(ls[2])
print(ls[0]+ls[1]*10+ls[2]*100)

