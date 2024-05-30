from typing import List

from printer import print_currency_info, print_phone_info


def group_and_print(phone_numbers: List[int]):
    cnt = 1
    for i in range(len(phone_numbers) - 1):
        if i == len(phone_numbers) - 2:
            if phone_numbers[i] == phone_numbers[i + 1]:
                cnt += 1
                print_phone_info(phone_numbers[i], cnt)
            else:
                print_phone_info(phone_numbers[i], cnt)
                print_phone_info(phone_numbers[i + 1], 1)
        elif phone_numbers[i] == phone_numbers[i + 1]:
            cnt += 1
        else:
            print_phone_info(phone_numbers[i], cnt)
            cnt = 1

def crypto_currency_analysis(file_contents: str):
    print("Input file contents: \n%s" % file_contents)
    records = file_contents.strip().split("\n")
    inv = []
    if len(records) == 1:
        print_currency_info(records[0].strip().split(":")[0], int(records[0].strip().split(":")[1]))

    for i in range(len(records) - 1):
        cur_coin, cur_inv = records[i].strip().split(":")
        next_coin = records[i + 1].strip().split(":")[0]
        inv.append(int(cur_inv))
        if i == len(records) - 2:
            if cur_coin != next_coin:
                print_currency_info(cur_coin, sum(inv) / len(inv))
                print_currency_info(next_coin, int(records[i + 1].split(":")[1]))
            else:
                inv.append(int(records[i + 1].split(":")[1]))
                print_currency_info(cur_coin, sum(inv) / len(inv))
        elif cur_coin != next_coin:
            print_currency_info(cur_coin, sum(inv) / len(inv))
            inv = []


if __name__ == "__main__":
    f = """
        BTC:42
                    BTC:600
                    BTC:900
                    DOGE:123456
                    DOGE:69420
                    ETH:220
                    ETH:666
                    XMR:14
                    XMR:88
        """
    crypto_currency_analysis(f)
