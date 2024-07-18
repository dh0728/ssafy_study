N = int(input())
li = list(map(int,input().split()))

print(f'{sorted(li)[0]} {sorted(li)[-1]}')