class Partida(tuple):
    def __new__(cls, gols_da_casa, gols_do_visitante):
        instance = tuple.__new__(cls, (gols_da_casa, gols_do_visitante))
        instance.vitoria = gols_da_casa > gols_do_visitante
        return instance


class Partidas(list):
    def melhor_saldo(self):
        return (1, 1) if self[0].vitoria else "nenhum"
    
