T = int(input())
days = [1, -2, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]

for i in range(T):
    a = input()
    year = int(a[:4])
    month = int(a[4:6])
    day = int(a[6:8])
    if 0<month<13 and day<=days[month-1]+30:
        print(f'#{i+1} {year:04}/{month:02}/{day:02}')
    else:
        print(f'#{i+1} -1')