from massa_dados import list_spend_money


def spend_by_login(login):
    for item in list_spend_money:
        if item[1] == login:
            print(item)

def sum_by_login(login):
    soma = float()
    for item in list_spend_money:
        if item[1] == login:
            soma += float(item[3]) if str(item[3]) else 0.0
    return soma


if __name__ == "__main__":
    login = 'justin16'
    spend_by_login(login)
    print('A soma total é: ')
    print(sum_by_login(login))
