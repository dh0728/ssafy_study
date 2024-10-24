n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # a 오름차순 정렬
s = 0 
for i in range(n):
    s += max(b) * a[i]
    b.remove(max(b)) 
print(s)