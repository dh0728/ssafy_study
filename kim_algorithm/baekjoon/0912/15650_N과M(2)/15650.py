N, M = map(int,input().split())


def dfs(depth, start, li):
    if depth == M:
        for i in li:
            print(i, end=" ")
        print()
        return

    for i in range(start, N+1):
        li.append(i)
        dfs(depth+1, i+1, li)
        li.pop()

dfs(0,1,[])