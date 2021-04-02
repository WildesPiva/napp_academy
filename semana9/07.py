def n_medias(*notas, **kwnotas):
    media = 0
    if notas:
        media = sum(notas)/float(len(notas))
    elif kwnotas:
        media = sum(kwnotas.values())/float(len(kwnotas))
    return media
