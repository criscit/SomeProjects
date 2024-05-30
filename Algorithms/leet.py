def hanoi_tower(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    elif n == 4:
        return 9
    else:
        return min(hanoi_tower(n - 4) + 15 + hanoi_tower(n - 4),
                   hanoi_tower(n - 3) + 7 + hanoi_tower(n - 3))





res_n_opt = []
for i in range(1, 11):
    res_n_opt.append(hanoi_tower(i))

pow_cnt = 1
pow = 1
cnt = 1
res = [1]
for i in range(2, 11):
    cnt += 2 ** pow
    res.append(cnt)
    if pow_cnt > pow:
        pow_cnt = 0
        pow += 1

    pow_cnt += 1

print(res_n_opt)
print(res)