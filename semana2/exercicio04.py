from massa_dados import list_spend_money

def spend_by_login(login, limit=1000):
    for item in list_spend_money:
        if item[1] == login:
            value = float(item[3]) if str(item[3]) else 0.0
            if value <= float(limit):
                print(item)

def sum_by_login(login, limit=1000):
    soma = float()
    for item in list_spend_money:
        if item[1] == login:
            value = float(item[3]) if str(item[3]) else 0.0
            if value <= float(limit):
                soma += value
    return soma


if __name__ == "__main__":
    login = 'justin16'
    spend_by_login(login, 1200)

    print('A soma total até 600: ')
    print(sum_by_login(login, 600))

    print('A soma total até 1200: ')
    print(sum_by_login(login, 1200))
