# Done
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

k_ls = []
for el in a:
    for i in range(len(str(el))):
        new_n = str(el)[0:i] + '9' + str(el)[i+1:]
        k_ls.append(int(new_n) - el)

k_ls.sort(reverse=True)
print(sum(k_ls[:k]))
