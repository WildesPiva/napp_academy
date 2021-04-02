def soma_numeros(*args):
    soma = 0
    for item in args:
        try:
            soma = soma + item
        except TypeError:
            raise TypeError('Incompatibilidade de tipos. Verificar parâmetros')
    return soma
