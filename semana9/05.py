def vacina_ja(idade, **kwargs):
    profissao_com_prioridade = ['medico', 'enfermeiro']
    profissao_com_prioridade += ['medica', 'enfermeira']
    profissao_com_prioridade += ['auxiliar de enfermagem']
    profissao_com_prioridade += ['profissionais da saude']
    profissao = kwargs.get('profissao', '').lower()
    if profissao in profissao_com_prioridade:
        return 'Autorizado Vacinação'
    if idade >= 69:
        return 'Autorizado Vacinação'
    if profissao == 'professor' and idade > 47:
        return 'Autorizado Vacinação'
    return 'Não autorizado por enquanto'
