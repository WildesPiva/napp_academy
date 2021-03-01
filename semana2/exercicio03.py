from massa_dados import list_spend_money


def spend_by_subname(name):
    for item in list_spend_money:
        if name in item[0]:
            print(item)

def sum_by_subname(name):
    soma = float()
    for item in list_spend_money:
        if name in item[0]:
            soma += float(item[3]) if str(item[3]) else 0.0
    return soma


if __name__ == "__main__":
    name = 'Brown'
    spend_by_subname(name)
    print('A soma total é: ')
    print(sum_by_subname(name))
