lista_nomes = ['Ana', 'Ana Maria', 'Pedro', 'Elena', 'Helena', 'Elen']
for nome in lista_nomes:
    letras = [l for l in nome]
    nome_pipe  = '|'.join(letras)
    print(f'|{nome_pipe}|')
