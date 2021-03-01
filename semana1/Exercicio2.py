lista_nomes = ['Ana', 'Maria', 'José', 'Pedro', 'Elena', 'Helena', 'elen']
for nome in lista_nomes:
    if nome[:1].lower() in ['a','e','i','o','u']:
        print(nome)