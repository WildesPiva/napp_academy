def juros_compostos(valor_inicial, juros, tempo):
    """
    Calculadora de juros compostos

    Args:
        valor_inicial (float): Valor inicial.
        juros (float): Porcentagem dos juros, entre 0% e 100%.
        tempo (int): Tempo em meses.
    """
    
    juros = float(juros)
    valor_inicial = float(valor_inicial)
    tempo = int(tempo)

    if juros < 0 or juros > 100:
        raise ValueError("Juros precisa estar entre 0 e 100")

    juros = juros/100
    valor_final = valor_inicial * (1+juros)**tempo
    return round(valor_final, 2)
