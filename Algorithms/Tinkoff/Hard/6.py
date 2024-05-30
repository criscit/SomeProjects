# Done
# Упростить при помощи массивов
n = int(input())
a = list(map(int, input().split()))

wrong_pos = {}
has_no_decision = False
for i in range(n):
    if (i % 2 == 0 and a[i] % 2 == 1) or (i % 2 == 1 and a[i] % 2 == 0):
        continue
    elif i % 2 == 1 and a[i] % 2 == 1:
        if 'even' not in wrong_pos:
            wrong_pos['even'] = i + 1
        else:
            has_no_decision = True
            break
    elif i % 2 == 0 and a[i] % 2 == 0:
        if 'odd' not in wrong_pos:
            wrong_pos['odd'] = i + 1
        else:
            has_no_decision = True
            break

if not has_no_decision and len(wrong_pos) == 2:
    print(*wrong_pos.values())
elif len(a) > 2 and len(wrong_pos) == 0:
    print(1, 3)
else:
    print(-1, -1)
