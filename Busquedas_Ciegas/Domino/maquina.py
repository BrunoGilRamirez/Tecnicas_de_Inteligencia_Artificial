class jugador_Maquina:
    tablero = []
    fichas = []
    #Algortimo utilizado: Best First Search
    def __init__(self, fichas, tablero): #constructor de la clase jugador_Maquina
        self.fichas = fichas #inicializa las fichas del jugador
        self.tablero = tablero #inicializa el tablero del jugador
    def actualizar_tablero(self, tablero): #actualiza el tablero del jugador
        self.tablero = tablero 
    def actualizar_fichas(self, fichas): #actualiza las fichas del jugador
        self.fichas = fichas #debido a que es el juego quien elimina las fichas, se actualizan las fichas del jugador
    
    def mejor_ficha(self, fichas): #retorna la mejor ficha para jugar, Se considera que esta es la funcion que implementa la heuristica, de que la ficha de mayor valor es la que se debe jugar
        mejor_ficha = fichas[0] #se inicializa la mejor ficha como la primera ficha de la lista de fichas
        for ficha in fichas: #se recorre la lista de fichas
            if ficha[0]+ficha[1] > mejor_ficha[0]+mejor_ficha[1]: #si la suma de los valores de la ficha actual es mayor a la suma de los valores de la mejor ficha, se actualiza la mejor ficha
                mejor_ficha = ficha #se actualiza la mejor ficha
        return mejor_ficha #se retorna la mejor ficha

    def fichas_posibles(self, Valorderecho, Valorizquierdo): #retorna las fichas que se pueden jugar en el tablero, esta es considerada la funcion sucessora
        fichas_posibles = [] #se inicializa la lista de fichas posibles
        for ficha in self.fichas: #se recorre la lista de fichas
            if ficha[0] == Valorderecho or ficha[1] == Valorderecho: #si el valor derecho de la ficha es igual al valor derecho del tablero o el valor izquierdo de la ficha es igual al valor derecho del tablero, se agrega la ficha a la lista de fichas posibles
                fichas_posibles.append(ficha) #se agrega la ficha a la lista de fichas posibles
            elif ficha[0] == Valorizquierdo or ficha[1] == Valorizquierdo: #si el valor izquierdo de la ficha es igual al valor izquierdo del tablero o el valor derecho de la ficha es igual al valor izquierdo del tablero, se agrega la ficha a la lista de fichas posibles
                fichas_posibles.append(ficha) #se agrega la ficha a la lista de fichas posibles
        return fichas_posibles #se retorna la lista de fichas posibles
    
    def jugar(self,fichas,tablero): #retorna la mejor ficha para jugar, esta es considerada la funcion objetivo
        self.actualizar_fichas(fichas) #se actualizan las fichas del jugador
        self.actualizar_tablero(tablero) #se actualiza el tablero del jugador
        if len(self.fichas)==0: #si el jugador no tiene fichas, retorna -1, hace una especie de funcion objetivo, que si no tiene fichas, retorna -1 y el juego termina
            return -1   
    
        Valorderecho = self.tablero[len(self.tablero)-1][1] #se obtiene el valor derecho del tablero
        Valorizquierdo = self.tablero[0][0] #se obtiene el valor izquierdo del tablero
        fichas_posibles = self.fichas_posibles(Valorderecho, Valorizquierdo) #se obtienen las fichas posibles
        
        if len(fichas_posibles) == 0: #si no hay fichas posibles, retorna -1, y se toma como un pasar turno, si ambos jugadores pasan turno, el juego termina
            return -1 
        else:
            return self.mejor_ficha(fichas_posibles) #si hay fichas posibles, retorna la mejor ficha para jugar
           