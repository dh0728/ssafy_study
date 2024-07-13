# 버전 1 
N = int(input())

li = list(map(int, input().split())) #리스트로 만들기

li.sort() #오름차순으로 정렬
num = (N-1)/2
print( li[int(num)])

# 버전 2
n=(int(input())-1)/2
a=list(map(int, input().split()))
a.sort()
print(a[int(n)])

# 버전 3
input()
a=list(map(int, input().split()))
a.sort()
print(a[len(a)//2])