from massa_dados import list_spend_money


def spend_by_gender(gender):
    for item in list_spend_money:
        if item[2] == gender:
            print(item)


def sum_by_gender(gender):
    soma = float()
    for item in list_spend_money:
        if item[2] == gender:
            soma += float(item[3]) if str(item[3]) else 0.0
    return soma


if __name__ == "__main__":
    gender = 'M'
    spend_by_gender(gender)
    print('A soma total é: ')
    print(sum_by_gender(gender))
