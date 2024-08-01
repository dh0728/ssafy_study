for s in range(5):
    for n in range(5):
        if s == n:
            print('#', end='')
        else:
            print('+', end='')

    print()