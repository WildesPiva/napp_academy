lista_frases = ['Eu gosto de batatas', 'Eu estava andando de moto']
lista_frases += ['Ele estava comendo no restaurante']
lista_frases += ['O cachorro está passeando pelo parque']
gerundios = ['ando', 'endo', 'indo']
for frase in lista_frases:
    for palavra in frase.split(' '):
        for gerundio in gerundios:
            if gerundio in palavra:
                print(palavra)
