class jugador_Maquina:
    tablero = []
    fichas = []
    def __init__(self, fichas, tablero):
        self.fichas = fichas
        self.tablero = tablero
    def actualizar_tablero(self, tablero):
        self.tablero = tablero
    def actualizar_fichas(self, fichas):
        self.fichas = fichas
    
    def mejor_ficha(self, fichas):
        mejor_ficha = fichas[0]
        for ficha in fichas:
            if ficha[0]+ficha[1] > mejor_ficha[0]+mejor_ficha[1]:
                mejor_ficha = ficha
        return mejor_ficha

    def jugar(self,fichas,tablero):
        self.actualizar_fichas(fichas)
        self.actualizar_tablero(tablero)
        if len(self.fichas)==0:
            return -1
        
        Valorderecho = self.tablero[len(self.tablero)-1][1]
        Valorizquierdo = self.tablero[0][0]
        fichas_posibles = []
        for ficha in self.fichas:
            if ficha[0] == Valorderecho or ficha[1] == Valorderecho:
                fichas_posibles.append(ficha)
            elif ficha[0] == Valorizquierdo or ficha[1] == Valorizquierdo:
                fichas_posibles.append(ficha)
        if len(fichas_posibles) == 0:
            return -1
        else:
            return self.mejor_ficha(fichas_posibles)
           