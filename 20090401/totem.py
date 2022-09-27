def achar_assinatura(totem, parte):
    if len(totem) == len(parte):
        return [(0,0)] if totem == parte else []
    elif len(totem) < len(parte):
        return []
    else:
        coordenadas = []
        andares = totem.split()
        for i, andar in enumerate(andares):
            posicao = andar.find(parte)
            if posicao != -1 :
                coordenadas.append((i,posicao))
        return coordenadas
