def situacao_escolar(nota_final, ausencias=0):
    if ausencias < 0 or ausencias > 80:
        raise Exception('Ausências entre 0 e 80')
    if nota_final < 0 or nota_final > 10:
        raise Exception('Nota Final entre 0 e 10')
    if ausencias > 40:
        return 'Reprovado por falta'
    if nota_final < 5:
        return 'Reprovado por nota'
    if nota_final < 7:
        return 'Reprovado, em regime de recuperação'
    return 'Aprovado'
