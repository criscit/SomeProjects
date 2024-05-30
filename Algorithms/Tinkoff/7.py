n = int(input())
a = list(map(int, input().split()))

ans = []
is_changed = False

if a[n-1] != 1:
    ans = [n, 1]
    is_changed = True

for i in range(n-1):
    if a[i] == i + 2:
        continue
    elif a[i] != i + 2 and not is_changed:
        ans = [i + 1, i + 2]
        is_changed = True
    else:
        ans = [-1, -1]
        break

print(*ans)