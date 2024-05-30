# Done
# Переделать только используя числа
l, r = list(map(int, input().split()))

max_len = len(str(r))
ans = 0
while max_len >= len(str(l)):
    for i in range(0, 10):
        n = int(str(i) * max_len)
        if l <= n <= r:
            ans += 1
        elif n > r:
            continue
        else:
            break

    max_len -= 1

print(ans)