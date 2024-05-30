def find_tink(s: str):
    search = 'tinkoff'
    out_s = ''
    i = 0
    for ch in s:
        if i < len(search) and ch == search[i]:
            i += 1
            ch = ch.upper()


        out_s += ch

    if i == len(search):
        return out_s
    else:
        return "IMPOSSIBLE"


t = int(input())
for i in range(t):
    in_s = input()
    print(find_tink(in_s))